import abc
from typing import List
from principle.solid.ocp.Product import Product
from principle.solid.ocp.good.Specification import Specification

"""
@File      : Filter.py   
@Author    : Rohit Agarwal on 24/11/21 10:18 pm
@Copyright : https://github.com/javamultiplex
"""


# TODO: explore generics
class Filter(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'filter') \
               and callable(subclass.filter) \
               or NotImplemented

    @abc.abstractmethod
    def filter(self, items: List[Product], specification: Specification) -> List[Product]:
        raise NotImplementedError
