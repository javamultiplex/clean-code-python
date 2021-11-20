from principle.solid.ocp.Color import Color
from principle.solid.ocp.Size import Size


class Product:
    def __init__(self, name: str, color: Color, size: Size) -> None:
        self._name = name
        self._color = color
        self._size = size

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def color(self) -> Color:
        return self._color

    @color.setter
    def color(self, new_color: Color):
        self._color = new_color

    @property
    def size(self) -> Size:
        return self._size

    @size.setter
    def size(self, new_size: Size):
        self._size = new_size

    def __str__(self) -> str:
        return self.name + "," + str(self.color) + "," + str(self.size)
