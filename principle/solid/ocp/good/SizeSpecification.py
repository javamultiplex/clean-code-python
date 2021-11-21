from principle.solid.ocp.Size import Size
from principle.solid.ocp.Product import Product


class SizeSpecification:
    def __init__(self, size: Size) -> None:
        self.size = size

    def isSatisfied(self, item: Product) -> bool:
        return self.size == item.size
