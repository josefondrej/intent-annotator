from typing import List

import pandas as pd


class Examples(object):
    def __init__(self):
        pass

    @property
    def examples(self) -> List[str]:
        return self._examples

    def load_from_excel(self, file):
        self._examples = list(pd.read_csv(file).iloc[:, 0])
        print(self._examples)
