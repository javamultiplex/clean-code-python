import unittest

from Rectangle import Rectangle
from Square import Square


class Tests(unittest.TestCase):
    def test_rectangle_area(self):
        rectangle = Rectangle(10, 20)
        area = rectangle.calculate_area()
        self.assertEqual(200, area)

    def test_square_area(self):
        square = Square(10)
        area = square.calculate_area()
        self.assertEqual(100, area)


if __name__ == '__main__':
    unittest.main()
