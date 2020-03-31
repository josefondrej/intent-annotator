from typing import Dict, List

from intent_annotator.core.file import File


class Workspace(File):
    def __init__(self):
        pass

    @property
    def json(self) -> Dict:
        return self.json_dict

    @property
    def intent_names(self) -> List[str]:
        raise NotImplementedError("TODO: Implement.")  # Cached possibly.

    def filter_intent_names(self, substring: str) -> List[str]:
        intents = self.intent_names
        return [intent for intent in intents if substring in intent]

    def get_intent_examples(self, intent_name: str) -> List[str]:
        raise NotImplementedError("TODO: Implement.")

    def add_intent_example(self, intent_name: str, example: str):
        raise NotImplementedError("TODO: Implement.")  # Check if it is not there already
