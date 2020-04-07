import json
import os
from typing import Dict, List, Union

import jsonpickle
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

    @classmethod
    def serialized_path(cls, id: str) -> str:
        return RESOURCES_PATH + id + "/" + cls.__name__ + ".json"

    @classmethod
    def load_jsonpickle(cls, id: str) -> "File":
        with open(cls.serialized_path(id)) as in_file:
            str_representation = in_file.read()
        return jsonpickle.loads(str_representation)

    def load_from_file_storage(self, file_storage: FileStorage):
        self._file_name = file_storage.filename
        file_storage.save(self.file_path)

        with open(self.file_path) as file:
            self._json_dict = json.load(file)

    def dump(self):
        with open(self.file_path, "w") as file:
            json.dump(self.json_dict, file, indent=4, separators=(',', ': '))

    def dump_jsonpickle(self):
        path = self.serialized_path(self.id)
        str_representation = jsonpickle.dumps(self)
        with open(path, "w") as out_file:
            out_file.write(str_representation)

    def _init_dir(self):
        path = RESOURCES_PATH + str(self.id) + "/"
        if not os.path.exists(path):
            os.mkdir(path)
