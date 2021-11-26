from typing import List

from principle.solid.ocp.Product import Product
from principle.solid.ocp.good.Specification import Specification

"""
@File      : OrSpecification.py   
@Author    : Rohit Agarwal on 24/11/21 10:18 pm
@Copyright : https://github.com/javamultiplex
"""


class OrSpecification(Specification):

    def __init__(self, specifications: List[Specification]):
        self.specifications = specifications

    def isSatisfied(self, item: Product) -> bool:
        result: bool = False
        for specification in self.specifications:
            result = result or specification.isSatisfied(item)
        return result
