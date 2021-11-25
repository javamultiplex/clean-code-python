from Shape import Shape

"""
@File      : Rectangle.py   
@Author    : Rohit Agarwal on 25/11/21 11:07 pm
@Copyright : https://github.com/javamultiplex
"""


class Rectangle(Shape):

    def __init__(self, height: int, width: int) -> None:
        self._height = height
        self._width = width

    def calculate_area(self) -> int:
        return self._height * self._width
