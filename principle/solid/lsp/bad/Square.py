from Rectangle import Rectangle

"""
@File      : Square.py   
@Author    : Rohit Agarwal on 24/11/21 10:34 pm
@Copyright : https://github.com/javamultiplex
"""


class Square(Rectangle):

    def __init__(self):
        Rectangle.__init__(self)

    def set_height(self, new_height: int) -> None:
        self._height = new_height
        self._width = new_height

    def set_width(self, new_width: int) -> None:
        self._height = new_width
        self._width = new_width
