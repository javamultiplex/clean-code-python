from principle.solid.ocp.Product import Product
from principle.solid.ocp.good.ColorSpecification import ColorSpecification
from principle.solid.ocp.good.SizeSpecification import SizeSpecification
from principle.solid.ocp.good.Specification import Specification

"""
@File      : AndSpecification.py   
@Author    : Rohit Agarwal on 24/11/21 10:18 pm
@Copyright : https://github.com/javamultiplex
"""


class AndSpecification(Specification):
    def __init__(self, color_specification: ColorSpecification, size_specification: SizeSpecification) -> None:
        self.color_specification = color_specification
        self.size_specification = size_specification

    def isSatisfied(self, item: Product) -> bool:
        return self.color_specification.isSatisfied(item) and self.size_specification.isSatisfied(item)
