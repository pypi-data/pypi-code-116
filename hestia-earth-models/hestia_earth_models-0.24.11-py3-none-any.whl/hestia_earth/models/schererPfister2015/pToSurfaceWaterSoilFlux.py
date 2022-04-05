from hestia_earth.schema import EmissionMethodTier, EmissionStatsDefinition

from hestia_earth.models.log import debugValues, logRequirements, logShouldRun
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.input import get_inorganic_fertilizer_P_total
from hestia_earth.models.utils.measurement import most_relevant_measurement_value
from . import MODEL
from .utils import get_liquid_slurry_sludge_P_total

TERM_ID = 'pToSurfaceWaterSoilFlux'
TIER = EmissionMethodTier.TIER_1.value


def _emission(value: float):
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = TIER
    emission['statsDefinition'] = EmissionStatsDefinition.MODELLED.value
    return emission


def _run(cycle: dict, slope: list, excreta_p_total: float):
    lss_P_total, not_lss_P_total = get_liquid_slurry_sludge_P_total(cycle)
    inorg_p_total = get_inorganic_fertilizer_P_total(cycle)
    value_slope = 0 if slope < 3 else 1

    debugValues(model=MODEL, term=TERM_ID,
                value_slope=value_slope,
                inorg_p_total=inorg_p_total,
                lss_P_total=lss_P_total,
                not_lss_P_total=not_lss_P_total)

    value = value_slope * (1 + (inorg_p_total * 0.2 + lss_P_total * 0.7 + (not_lss_P_total + excreta_p_total) * 0.4)/80)
    return [_emission(value)]


def _should_run(cycle: dict):
    end_date = cycle.get('endDate')
    site = cycle.get('site', {})
    measurements = site.get('measurements', [])
    slope = most_relevant_measurement_value(measurements, 'slope', end_date)
    # TODO: add excreta as input when is gone onto pasture
    excreta_p_total = 0

    logRequirements(model=MODEL, term=TERM_ID,
                    slope=slope)

    should_run = all([slope])
    logShouldRun(MODEL, TERM_ID, should_run, methodTier=TIER)
    return should_run, slope, excreta_p_total


def run(cycle: dict):
    should_run, slope, excreta_p_total = _should_run(cycle)
    return _run(cycle, slope, excreta_p_total) if should_run else []
