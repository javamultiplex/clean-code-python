import abc

"""
@File      : Shape.py   
@Author    : Rohit Agarwal on 25/11/21 11:00 pm
@Copyright : https://github.com/javamultiplex
"""


class Shape(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'calculate_area') \
               and callable(subclass.calculate_area) \
               or NotImplemented

    @abc.abstractmethod
    def calculate_area(self) -> int:
        raise NotImplementedError
