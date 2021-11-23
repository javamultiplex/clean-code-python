import abc
from principle.solid.ocp.Product import Product


class Specification(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'isSatisfied') \
               and callable(subclass.isSatisfied) \
               or NotImplemented

    @abc.abstractmethod
    def isSatisfied(self, item: Product) -> bool:
        raise NotImplementedError
