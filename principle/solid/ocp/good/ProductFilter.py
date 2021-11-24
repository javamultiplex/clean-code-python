from typing import List

from principle.solid.ocp.Product import Product
from principle.solid.ocp.good.Filter import Filter
from principle.solid.ocp.good.Specification import Specification

"""
@File      : ProductFilter.py   
@Author    : Rohit Agarwal on 24/11/21 10:18 pm
@Copyright : https://github.com/javamultiplex
"""


class ProductFilter(Filter):
    def filter(self, items: List[Product], specification: Specification) -> List[Product]:
        result: List[Product] = []
        for item in items:
            if specification.isSatisfied(item):
                result.append(item)
        return result
