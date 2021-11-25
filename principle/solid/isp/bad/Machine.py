import abc
from principle.solid.isp.Document import Document

"""
@File      : Machine.py   
@Author    : Rohit Agarwal on 25/11/21 11:26 pm
@Copyright : https://github.com/javamultiplex
"""


class Machine(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "print") \
               and callable(subclass.print) \
               and hasattr(subclass, "scan") \
               and callable(subclass.scan) \
               and hasattr(subclass, "fax") \
               and callable(subclass.fax)

    @abc.abstractmethod
    def print(self, document: Document) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def scan(self, document: Document) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def fax(self, document: Document) -> None:
        raise NotImplementedError
