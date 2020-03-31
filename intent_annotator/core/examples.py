from typing import List

from intent_annotator.core.file import File


class Examples(File):
    def __init__(self):
        pass

    @property
    def examples(self) -> List[str]:
        return self._examples

