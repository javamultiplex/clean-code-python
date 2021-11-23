import abc
from typing import List
from principle.solid.ocp.Product import Product
from principle.solid.ocp.good.Specification import Specification


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
