"""Config flow for Min/Max integration."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, cast

import voluptuous as vol

from homeassistant.const import CONF_TYPE
from homeassistant.helpers import selector
from homeassistant.helpers.schema_config_entry_flow import (
    SchemaConfigFlowHandler,
    SchemaFlowFormStep,
    SchemaFlowMenuStep,
)

from .const import CONF_ENTITY_IDS, CONF_ROUND_DIGITS, DOMAIN

_STATISTIC_MEASURES = [
    {"value": "min", "label": "Minimum"},
    {"value": "max", "label": "Maximum"},
    {"value": "mean", "label": "Arithmetic mean"},
    {"value": "median", "label": "Median"},
    {"value": "last", "label": "Most recently updated"},
]


OPTIONS_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ENTITY_IDS): selector.selector(
            {"entity": {"domain": "sensor", "multiple": True}}
        ),
        vol.Required(CONF_TYPE): selector.selector(
            {"select": {"options": _STATISTIC_MEASURES}}
        ),
        vol.Required(CONF_ROUND_DIGITS, default=2): selector.selector(
            {"number": {"min": 0, "max": 6, "mode": "box"}}
        ),
    }
)

CONFIG_SCHEMA = vol.Schema(
    {
        vol.Required("name"): selector.selector({"text": {}}),
    }
).extend(OPTIONS_SCHEMA.schema)

CONFIG_FLOW: dict[str, SchemaFlowFormStep | SchemaFlowMenuStep] = {
    "user": SchemaFlowFormStep(CONFIG_SCHEMA)
}

OPTIONS_FLOW: dict[str, SchemaFlowFormStep | SchemaFlowMenuStep] = {
    "init": SchemaFlowFormStep(OPTIONS_SCHEMA)
}


class ConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    """Handle a config or options flow for Min/Max."""

    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW

    def async_config_entry_title(self, options: Mapping[str, Any]) -> str:
        """Return config entry title."""
        return cast(str, options["name"]) if "name" in options else ""
