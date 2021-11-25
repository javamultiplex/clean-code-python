from Shape import Shape

"""
@File      : Square.py   
@Author    : Rohit Agarwal on 25/11/21 11:09 pm
@Copyright : https://github.com/javamultiplex
"""


class Square(Shape):

    def __init__(self, side: int) -> None:
        self._side = side

    def calculate_area(self) -> int:
        return self._side * self._side
