from typing import Dict, List

from intent_annotator.core.file import File

FIELD_INTENT = "intent"
FIELD_INTENTS = "intents"
FIELD_EXAMPLES = "examples"
FIELD_TEXT = "text"

class Workspace(File):
    @property
    def intent_names(self) -> List[str]:
        names = [intent[FIELD_INTENT] for intent in self.json_dict[FIELD_INTENTS]]
        return names

    @property
    def intent_examples(self) -> List[str]:
        examples = []
        intent_dict = self.json_dict[FIELD_INTENTS]
        for intent in intent_dict:
            intent_examples = [ex[FIELD_TEXT] for ex in intent[FIELD_EXAMPLES]]
            examples.extend(intent_examples)

        return examples

    def filter_intent_names(self, substring: str) -> List[str]:
        intents = self.intent_names
        return [intent for intent in intents if substring in intent]

    def get_intent_examples(self, intent_name: str) -> List[str]:
        raise NotImplementedError("TODO: Implement.")

    def add_intent_example(self, intent_name: str, example: str):
        example_dict = self._create_example_dict(example)
        intent_dict = self._find_intent_dict(intent_name)
        examples = intent_dict[FIELD_EXAMPLES]
        if example not in [ex[FIELD_TEXT] for ex in examples]:
            intent_dict[FIELD_EXAMPLES].append(example_dict)

    def _create_intent_dict(self, intent_name: str) -> Dict:
        return {FIELD_INTENT: intent_name, FIELD_EXAMPLES: []}

    def _create_example_dict(self, example: str) -> Dict:
        return {FIELD_TEXT: example}

    def _find_intent_dict(self, intent_name: str) -> Dict:
        for intent_dict in self.json_dict[FIELD_INTENTS]:
            if intent_dict[FIELD_INTENT] == intent_name:
                return intent_dict

        intent_dict = self._create_intent_dict(intent_name)
        self.json_dict[FIELD_INTENTS].append(intent_dict)
        return intent_dict
