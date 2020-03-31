from intent_annotator.core.examples import Examples
from intent_annotator.core.workspace import Workspace


class Annotator(object):
    def __init__(self, workspace: Workspace, examples: Examples):
        self._workspace = workspace
        self._examples = examples

    @property
    def examples(self):
        return self._examples.examples

    def get_example(self, example_index: int) -> str:
        return self._examples.examples[example_index]

    def annotate_example(self, example: str, intent_name: str):
        self._workspace.add_intent_example(intent_name, example)
