import abc

from principle.solid.ocp.Product import Product

"""
@File      : Specification.py   
@Author    : Rohit Agarwal on 24/11/21 10:18 pm
@Copyright : https://github.com/javamultiplex
"""


class Specification(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'isSatisfied') \
               and callable(subclass.isSatisfied) \
               or NotImplemented

    @abc.abstractmethod
    def isSatisfied(self, item: Product) -> bool:
        raise NotImplementedError
