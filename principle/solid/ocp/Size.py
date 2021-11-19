import enum


class Size(enum.Enum):
    SMALL = 1
    LARGE = 2
    MEDIUM = 3


if __name__ == '__main__':
    print(str(Size.LARGE))
    print(repr(Size.LARGE))
    print(type(Size.LARGE))
    print(Size.LARGE.name)