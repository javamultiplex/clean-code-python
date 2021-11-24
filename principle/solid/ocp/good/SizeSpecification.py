from principle.solid.ocp.Size import Size
from principle.solid.ocp.Product import Product
from principle.solid.ocp.good.Specification import Specification

"""
@File      : SizeSpecification.py   
@Author    : Rohit Agarwal on 24/11/21 10:18 pm
@Copyright : https://github.com/javamultiplex
"""


class SizeSpecification(Specification):
    def __init__(self, size: Size) -> None:
        self.size = size

    def isSatisfied(self, item: Product) -> bool:
        return self.size == item.size
