import abc

from principle.solid.isp.Document import Document

"""
@File      : Fax.py   
@Author    : Rohit Agarwal on 26/11/21 9:34 pm
@Copyright : https://github.com/javamultiplex
"""


class Fax(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "fax") \
               and callable(subclass.fax)

    @abc.abstractmethod
    def fax(self, document: Document) -> None:
        raise NotImplementedError
