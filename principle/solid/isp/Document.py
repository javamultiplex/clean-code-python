"""
@File      : Document.py   
@Author    : Rohit Agarwal on 25/11/21 11:19 pm
@Copyright : https://github.com/javamultiplex
"""


class Document:
    _name: str = None
    _size: int = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        self._size = new_size

    def __str__(self) -> str:
        return "Document[" + self.name + str(self.size) + "]"
