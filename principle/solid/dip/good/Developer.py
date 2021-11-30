import abc

"""
@File      : Developer.py   
@Author    : Rohit Agarwal on 30/11/21 11:11 pm
@Copyright : https://github.com/javamultiplex
"""


class Developer(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "develop") and callable(subclass.develop)

    @abc.abstractmethod
    def develop(self) -> None:
        raise NotImplementedError
