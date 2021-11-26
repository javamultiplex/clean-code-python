import abc

from principle.solid.isp.Document import Document

"""
@File      : Printer.py   
@Author    : Rohit Agarwal on 26/11/21 9:34 pm
@Copyright : https://github.com/javamultiplex
"""


class Printer(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "print") \
               and callable(subclass.print)

    @abc.abstractmethod
    def print(self, document: Document) -> None:
        raise NotImplementedError
