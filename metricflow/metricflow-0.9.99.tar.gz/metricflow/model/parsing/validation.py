import logging

import yaml
from jsonschema import exceptions

from metricflow.errors.errors import ParsingException
from metricflow.model.parsing.schemas_internal import (
    metric_validator,
    data_source_validator,
    materialization_validator,
)

VERSION_KEY = "version"
METRIC_TYPE = "metric"
DATA_SOURCE_TYPE = "data_source"
MATERIALIZATION_TYPE = "materialization"
DERIVED_GROUP_BY_ELEMENT_TYPE = "derived_identifier"
DOCUMENT_TYPES = [METRIC_TYPE, DATA_SOURCE_TYPE, MATERIALIZATION_TYPE]

logger = logging.getLogger(__name__)


def validate_config_structure(contents: str) -> None:  # noqa: D
    """Validates config shape against jsonschema

    catches ValidationError and raise one exception at the end so
    we can get all the validation errors rather than just the first
    """
    errors = []
    for config_document in yaml.load_all(contents, Loader=yaml.SafeLoader):
        # The config document can be None if there is nothing but white space between two `---`
        # this isn't really an issue, so lets just swallow it
        if config_document is None:
            continue
        if not isinstance(config_document, dict):
            errors.append(
                str(
                    ParsingException(
                        f"Transform object yaml must be a dict. Got `{type(config_document)}`: {config_document}",
                    )
                )
            )
            continue
        for document_type in config_document.keys():
            try:
                if document_type == METRIC_TYPE:
                    metric_validator.validate(config_document[document_type])
                elif document_type == DATA_SOURCE_TYPE:
                    data_source_validator.validate(config_document[document_type])
                elif document_type == MATERIALIZATION_TYPE:
                    materialization_validator.validate(config_document[document_type])
                elif document_type == DERIVED_GROUP_BY_ELEMENT_TYPE:
                    logger.warning(f"{DERIVED_GROUP_BY_ELEMENT_TYPE} is not supported")
                elif document_type == VERSION_KEY:
                    pass
                else:
                    raise ParsingException(f"No valid document type detected. got: {document_type}")
            except exceptions.ValidationError as e:
                errors.append(f"{e}")
                logger.exception(str(e))

    if len(errors) > 0:
        raise exceptions.ValidationError("\n".join(errors))
