import json
from typing import Dict, List


class Workspace(object):
    def __init__(self):
        pass

    @property
    def json(self) -> Dict:
        return self._workspace_json

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

    def dump(self):
        with open(self._workspace_json_path, "w") as workspace_file:
            json.dump(self._workspace_json, workspace_file)

    def load(self, file):
        self._workspace_json = json.load(file)
