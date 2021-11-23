from principle.solid.ocp.good.Specification import Specification
from principle.solid.ocp.Product import Product
from typing import List


class OrSpecification(Specification):

    def __init__(self, specifications: List[Specification]):
        self.specifications = specifications

    def isSatisfied(self, item: Product) -> bool:
        result: bool = False
        for specification in self.specifications:
            result = result or specification.isSatisfied(item)
        return result
