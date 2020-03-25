import json
from typing import Dict, List


class Workspace(object):
    def __init__(self, workspace_json_path: str):
        self._workspace_json_path = workspace_json_path
        self._workspace_json = self.load(self._workspace_json_path)

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

    def load(self, file_path: str) -> Dict:
        with open(file_path, "r") as file:
            workspace_json = json.dump(file)
        return workspace_json
