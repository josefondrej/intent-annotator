import json
import os
from typing import Dict, List, Union

from werkzeug.datastructures import FileStorage

from intent_annotator.utils.abs_paths import RESOURCES_PATH


class File(object):
    def __init__(self, id: str = None):
        self._id = id
        self._init_dir()

    @property
    def id(self) -> str:
        return self._id

    @property
    def file_path(self) -> str:
        return RESOURCES_PATH + self.relative_file_path

    @property
    def relative_file_path(self) -> str:
        return self.id + "/" + self._file_name

    @property
    def file_name(self) -> str:
        return self._file_name

    @property
    def json_dict(self) -> Union[List, Dict]:
        return self._json_dict

    def load_from_file_storage(self, file_storage: FileStorage):
        self._file_name = file_storage.filename
        file_storage.save(self.file_path)

        with open(self.file_path) as file:
            self._json_dict = json.load(file)

    def dump(self):
        with open(self.file_path, "w") as file:
            json.dump(self.json_dict, file, indent=4, separators=(',', ': '))

    def _init_dir(self):
        path = RESOURCES_PATH + str(self.id) + "/"
        if not os.path.exists(path):
            os.mkdir(path)
