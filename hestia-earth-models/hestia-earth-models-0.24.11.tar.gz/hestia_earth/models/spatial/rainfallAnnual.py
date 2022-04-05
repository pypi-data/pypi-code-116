from hestia_earth.schema import MeasurementStatsDefinition
from datetime import datetime
from dateutil.relativedelta import relativedelta
from hestia_earth.utils.tools import non_empty_list

from hestia_earth.models.log import logRequirements, logShouldRun, logger
from hestia_earth.models.utils.measurement import _new_measurement
from hestia_earth.models.utils.cycle import cycle_end_year
from hestia_earth.models.utils.site import related_cycles
from .utils import MAX_AREA_SIZE, download, find_existing_measurement, has_geospatial_data, should_download
from . import MODEL

TERM_ID = 'rainfallAnnual'
EE_PARAMS = {
    'collection': 'ECMWF/ERA5/MONTHLY',
    'ee_type': 'raster_by_period',
    'reducer': 'sum',
    'band_name': 'total_precipitation'
}
BIBLIO_TITLE = 'ERA5: Fifth generation of ECMWF atmospheric reanalyses of the global climate'


def _cycle_valid(year: int):
    # NOTE: Currently uses the climate data for the final year of the study
    # see: https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_MONTHLY
    # ERA5 data is available from 1979 to three months from real-time
    limit_upper = datetime.now() + relativedelta(months=-3)
    return 1979 <= year and year <= limit_upper.year


def _measurement(value: float, year: int):
    measurement = _new_measurement(TERM_ID, MODEL, BIBLIO_TITLE)
    measurement['value'] = [value]
    measurement['statsDefinition'] = MeasurementStatsDefinition.SPATIAL.value
    measurement['startDate'] = f"{year}-01-01"
    measurement['endDate'] = f"{year}-12-31"
    return measurement


def _download(site: dict, year: int):
    # collection is in meters, convert to millimeters
    factor = 1000
    reducer_regions = 'mean'
    return download(
        TERM_ID,
        site,
        {
            **EE_PARAMS,
            'reducer_regions': reducer_regions,
            'year': str(year)
        }
    ).get(reducer_regions, 0) * factor


def _run(site: dict, year: int):
    value = find_existing_measurement(TERM_ID, site, year) or _download(site, year)
    return _measurement(value, year) if value else None


def _should_run(site: dict, year: int):
    geospatial_data = has_geospatial_data(site)
    below_max_area_size = should_download(site)
    valid_year = _cycle_valid(year)

    logRequirements(model=MODEL, term=TERM_ID,
                    geospatial_data=geospatial_data,
                    max_area_size=MAX_AREA_SIZE,
                    below_max_area_size=below_max_area_size,
                    valid_year=valid_year)

    should_run = all([geospatial_data, below_max_area_size, valid_year])
    logShouldRun(MODEL, TERM_ID, should_run)
    return should_run


def run(site: dict):
    cycles = related_cycles(site.get('@id'))
    has_related_cycles = len(cycles) > 0

    logRequirements(model=MODEL, term=TERM_ID,
                    has_related_cycles=has_related_cycles)

    logger.debug('model=%s, term=%s, related_cycles=%s', MODEL, TERM_ID, ','.join(map(lambda c: c.get('@id'), cycles)))
    years = non_empty_list(set(map(cycle_end_year, cycles)))
    years = list(filter(lambda year: _should_run(site, year), years))
    logger.debug('model=%s, term=%s, years=%s', MODEL, TERM_ID, years)
    return non_empty_list(map(lambda year: _run(site, year), years))
