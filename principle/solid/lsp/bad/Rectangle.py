"""
@File      : Rectangle.py   
@Author    : Rohit Agarwal on 24/11/21 10:26 pm
@Copyright : https://github.com/javamultiplex
"""


class Rectangle:
    _height: int = None
    _width: int = None

    def set_height(self, new_height: int) -> None:
        self._height = new_height

    def get_height(self) -> int:
        return self._height

    def set_width(self, new_width: int) -> None:
        self._width = new_width

    def get_width(self) -> int:
        return self._width

    def calculate_area(self) -> int:
        return self._height * self._width
