from io import TextIOWrapper
from typing import Optional, Union

File = tuple[Optional[str], Union[bytes, str, TextIOWrapper]]
UploadFile = dict[str, File]


class ParsableObject(object):
    def __init__(self, view: dict) -> None:
        self._view = view
        self.parse()