import abc


class Specification(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'isSatisfied') and callable(subclass.isSatisfied)
