from typing import List
from principle.solid.ocp.Color import Color
from principle.solid.ocp.Product import Product
from principle.solid.ocp.Size import Size


def filterByColor(products: List[Product], color: Color) -> List[str]:
    result: List[str] = []
    for product in products:
        if product.color == color:
            result.append(product.name)
    return result


if __name__ == '__main__':
    p1 = Product("Mango", Color.GREEN, Size.LARGE)
    p2 = Product("Apple", Color.RED, Size.SMALL)
    p3 = Product("Tree", Color.GREEN, Size.LARGE)
    output = filterByColor([p1, p2, p3], Color.RED)
    print(output)
