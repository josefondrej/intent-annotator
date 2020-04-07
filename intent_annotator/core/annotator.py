from typing import List

from intent_annotator.core.examples import Examples
from intent_annotator.core.workspace import Workspace


class Annotator(object):
    def __init__(self, workspace: Workspace, examples: Examples):
        self._workspace = workspace
        self._examples = examples

    @property
    def examples(self) -> List[str]:
        try:
            return list(set(self._examples.examples) - set(self._workspace.intent_examples))
        except:
            return []

    @property
    def all_examples(self) -> List[str]:
        return list(set(self._examples.examples))

    @property
    def intent_names(self):
        return self._workspace.intent_names

    def get_example(self, example_index: int) -> str:
        return self._examples.examples[example_index]

    def annotate_example(self, example: str, intent_name: str):
        self._workspace.add_intent_example(intent_name, example)

    def dump_workspace(self):
        try:
            self._workspace.dump()
        except:
            pass

    def dump_workspace_jsonpickle(self):
        self._workspace.dump_jsonpickle()
