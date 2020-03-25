from typing import List

import pandas as pd


class Examples(object):
    def __init__(self, examples_file_path: str):
        self._examples_file_path = examples_file_path
        self._examples = self._load_excel(self._examples_file_path)

    @property
    def examples(self) -> List[str]:
        return self._examples

    def _load_excel(self, file_path: str) -> List[str]:
        examples = pd.read_excel(file_path)
        return examples
