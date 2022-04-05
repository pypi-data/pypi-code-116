import logging
import os
from typing import Any, Dict, List, Optional, Text, Tuple

from neuralspace.nlu.converters.rasa.formats.readerwriter import TrainingDataReader
from neuralspace.nlu.converters.rasa.message import Message
from neuralspace.nlu.converters.rasa.shared.constants import DOCS_BASE_URL
from neuralspace.nlu.converters.rasa.shared.io import raise_warning, read_json_file

logger = logging.getLogger(__name__)

DOCS_URL_MIGRATE_GOOGLE = DOCS_BASE_URL + "/migrate-from/google-dialogflow-to-rasa/"

DIALOGFLOW_PACKAGE = "dialogflow_package"
DIALOGFLOW_AGENT = "dialogflow_agent"
DIALOGFLOW_INTENT = "dialogflow_intent"
DIALOGFLOW_INTENT_EXAMPLES = "dialogflow_intent_examples"
DIALOGFLOW_ENTITIES = "dialogflow_entities"
DIALOGFLOW_ENTITY_ENTRIES = "dialogflow_entity_entries"


class DialogflowReader(TrainingDataReader):
    def read(self, fn: Text, **kwargs: Any) -> "TrainingData":  # noqa : F821
        """Loads training data stored in the Dialogflow data format."""

        from neuralspace.nlu.converters.rasa.training_data.training_data import (
            TrainingData,
        )

        language = kwargs["language"]
        fformat = kwargs["fformat"]

        if fformat not in {DIALOGFLOW_INTENT, DIALOGFLOW_ENTITIES}:
            raise ValueError(
                "fformat must be either {}, or {}"
                "".format(DIALOGFLOW_INTENT, DIALOGFLOW_ENTITIES)
            )

        root_js = read_json_file(fn)
        examples = self._read_examples(fn, language, fformat)

        if not examples:
            raise_warning(
                f"No training examples found for dialogflow file {fn}!",
                docs=DOCS_URL_MIGRATE_GOOGLE,
            )
            return TrainingData()
        elif fformat == DIALOGFLOW_INTENT:
            return self._read_intent(root_js, examples)
        else:  # path for DIALOGFLOW_ENTITIES
            return self._read_entities(root_js, examples)

    def _read_intent(
        self, intent: Dict[Text, Any], examples: List[Dict[Text, Any]]
    ) -> "TrainingData":  # noqa : F821
        from neuralspace.nlu.converters.rasa.training_data.training_data import (
            TrainingData,
        )

        """Reads the intent and examples from respective jsons."""
        intent = intent.get("name")

        training_examples = []
        for ex in examples:
            text, entities = self._join_text_chunks(ex["data"])
            training_examples.append(Message.build(text, intent, entities))

        return TrainingData(training_examples)

    def _join_text_chunks(
        self, chunks: List[Dict[Text, Any]]
    ) -> Tuple[Text, List[Dict[Text, Any]]]:
        """Combines text chunks and extracts entities."""
        utterance = ""
        entities = []
        for chunk in chunks:
            entity = self._extract_entity(chunk, len(utterance))
            if entity:
                entities.append(entity)
            utterance += chunk["text"]

        return utterance, entities

    @staticmethod
    def _extract_entity(
        chunk: Dict[Text, Any], current_offset: int
    ) -> Optional[Dict[Text, Any]]:
        from neuralspace.nlu.converters.rasa.util import build_entity

        """Extract an entity from a chunk if present."""
        entity = None
        if "meta" in chunk or "alias" in chunk:
            start = current_offset
            text = chunk["text"]
            end = start + len(text)
            entity_type = chunk.get("alias", chunk["meta"])
            if entity_type != "@sys.ignore":
                entity = build_entity(start, end, text, entity_type)

        return entity

    @staticmethod
    def _flatten(list_of_lists: List[List[Any]]) -> List[Any]:
        return [item for items in list_of_lists for item in items]

    @staticmethod
    def _extract_lookup_tables(
        entity: Dict[Text, Any], examples: List[Dict[Text, Any]]
    ) -> Optional[List[Dict[Text, Any]]]:
        """Extracts the lookup table from the entity synonyms."""
        synonyms = [e["synonyms"] for e in examples if "synonyms" in e]
        synonyms = DialogflowReader._flatten(synonyms)
        elements = [synonym for synonym in synonyms if "@" not in synonym]

        if len(elements) == 0:
            return None
        return [{"name": entity.get("name"), "elements": elements}]

    @staticmethod
    def _extract_regex_features(
        entity: Dict[Text, Any], examples: List[Dict[Text, Any]]
    ) -> List[Dict[Text, Any]]:
        """Extract the regex features from the entity synonyms."""
        synonyms = [e["synonyms"] for e in examples if "synonyms" in e]
        synonyms = DialogflowReader._flatten(synonyms)
        return [
            {"name": entity.get("name"), "pattern": synonym} for synonym in synonyms
        ]

    @staticmethod
    def _read_entities(
        entity: Dict[Text, Any], examples: List[Dict[Text, Any]]
    ) -> "TrainingData":  # noqa : F821
        from neuralspace.nlu.converters.rasa.training_data.training_data import (
            TrainingData,
        )
        from neuralspace.nlu.converters.rasa.util import transform_entity_synonyms

        entity_synonyms = transform_entity_synonyms(examples)

        if entity["isRegexp"]:
            regex_features = DialogflowReader._extract_regex_features(entity, examples)
            return TrainingData(
                [],
                entity_synonyms,
                regex_features,
                [],
            )
        else:
            lookup_tables = DialogflowReader._extract_lookup_tables(entity, examples)
            return TrainingData(
                [],
                entity_synonyms,
                [],
                lookup_tables,
            )

    @staticmethod
    def _read_examples(
        fn: Text, language: Text, fformat: Text
    ) -> Optional[List[Dict[Text, Any]]]:
        """Infer and load the example file based on the root
        filename and root format."""

        if fformat == DIALOGFLOW_INTENT:
            examples_type = "usersays"
        else:
            examples_type = "entries"
        examples_fn_ending = f"_{examples_type}_{language}.json"
        examples_fn = fn.replace(".json", examples_fn_ending)
        if os.path.isfile(examples_fn):
            return read_json_file(examples_fn)
        else:
            return None

    def reads(self, s: Text, **kwargs: Any) -> "TrainingData":  # noqa : F821
        raise NotImplementedError
