from typing import List
from principle.solid.ocp.Color import Color
from principle.solid.ocp.Product import Product
from principle.solid.ocp.Size import Size


def filterByColor(products: List[Product], color: Color) -> List[Product]:
    result: List[Product] = []
    for product in products:
        if product.color == color:
            result.append(product)
    return result


def filterBySize(products: List[Product], size: Size) -> List[Product]:
    result: List[Product] = []
    for product in products:
        if product.size == size:
            result.append(product)
    return result


def filterBySizeAndColor(products: List[Product], size: Size, color: Color) -> List[Product]:
    result: List[Product] = []
    for product in products:
        if product.size == size and product.color == color:
            result.append(product)
    return result


if __name__ == '__main__':
    p1 = Product("Mango", Color.GREEN, Size.LARGE)
    p2 = Product("Apple", Color.RED, Size.SMALL)
    p3 = Product("Tree", Color.GREEN, Size.LARGE)
    p4 = Product("House", Color.BLUE, Size.SMALL)
    output = filterByColor([p1, p2, p3, p4], Color.GREEN)
    print(*output, sep="\n")
    print("**************************")
    output = filterBySize([p1, p2, p3, p4], Size.SMALL)
    print(*output, sep="\n")
    print("**************************")
    output = filterBySizeAndColor([p1, p2, p3, p4], Size.SMALL, Color.BLUE)
    print(*output, sep="\n")
