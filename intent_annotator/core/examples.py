from typing import List

from werkzeug.datastructures import FileStorage

from intent_annotator.core.file import File


class Examples(File):
    def __init__(self):
        pass

    @property
    def examples(self) -> List[str]:
        return self.json_dict

    def _hacky_line_reformat(self, line: str) -> str:
        line = line.strip()
        if line.startswith("["):
            line = line[1:]
        return line[1:-2]

    def load_from_file_storage(self, file_storage: FileStorage):
        self._file_name = file_storage.filename
        file_storage.save(self.file_path)

        with open(self.file_path) as file:
            self._json_dict = file.readlines()
            self._json_dict = [self._hacky_line_reformat(line) for line in self._json_dict]
