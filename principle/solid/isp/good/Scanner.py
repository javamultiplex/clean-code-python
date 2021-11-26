import abc

from principle.solid.isp.Document import Document

"""
@File      : Scanner.py   
@Author    : Rohit Agarwal on 26/11/21 9:34 pm
@Copyright : https://github.com/javamultiplex
"""


class Scanner(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "scan") \
               and callable(subclass.scan)

    @abc.abstractmethod
    def scan(self, document: Document) -> None:
        raise NotImplementedError
