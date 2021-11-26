from typing import List

from principle.solid.ocp.Color import Color
from principle.solid.ocp.Product import Product
from principle.solid.ocp.Size import Size
from principle.solid.ocp.good.AndSpecification import AndSpecification
from principle.solid.ocp.good.ColorSpecification import ColorSpecification
from principle.solid.ocp.good.OrSpecification import OrSpecification
from principle.solid.ocp.good.ProductFilter import ProductFilter
from principle.solid.ocp.good.SizeSpecification import SizeSpecification

"""
@File      : Main.py   
@Author    : Rohit Agarwal on 24/11/21 10:18 pm
@Copyright : https://github.com/javamultiplex
"""

if __name__ == '__main__':
    p1 = Product("Mango", Color.GREEN, Size.LARGE)
    p2 = Product("Apple", Color.RED, Size.SMALL)
    p3 = Product("Tree", Color.GREEN, Size.LARGE)
    p4 = Product("House", Color.BLUE, Size.SMALL)

    productFilter = ProductFilter()
    print("**** filter by color *****")
    output: List[Product] = productFilter.filter([p1, p2, p3, p4], ColorSpecification(Color.GREEN))
    print(*output, sep="\n")

    print("**** filter by size *****")
    output: List[Product] = productFilter.filter([p1, p2, p3, p4], SizeSpecification(Size.SMALL))
    print(*output, sep="\n")

    print("**** filter by size and color*****")
    output: List[Product] = productFilter.filter([p1, p2, p3, p4], AndSpecification(ColorSpecification(Color.RED),
                                                                                    SizeSpecification(Size.SMALL)))
    print(*output, sep="\n")

    print("**** filter by size or color*****")
    output: List[Product] = productFilter.filter([p1, p2, p3, p4], OrSpecification(
        [SizeSpecification(Size.SMALL), ColorSpecification(Color.RED)]))
    print(*output, sep="\n")
