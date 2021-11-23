from principle.solid.ocp.Color import Color
from principle.solid.ocp.Product import Product
from principle.solid.ocp.good.Specification import Specification


class ColorSpecification(Specification):
    def __init__(self, color: Color) -> None:
        self.color = color

    def isSatisfied(self, item: Product) -> bool:
        return self.color == item.color
