class Product:
    def __init__(self, name, color, size):
        self._name = name
        self._color = color
        self._size = size

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name = newName

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, newColor):
        self._color = newColor

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, newSize):
        self._size = newSize
