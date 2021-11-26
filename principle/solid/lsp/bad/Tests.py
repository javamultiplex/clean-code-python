import unittest

from Rectangle import Rectangle
from Square import Square


class Tests(unittest.TestCase):
    def test_rectangle_area(self):
        rectangle = Rectangle()
        rectangle.set_width(10)
        rectangle.set_height(20)
        area = rectangle.calculate_area()
        self.assertEqual(200, area)

    def test_square_area(self):
        square = Square()
        square.set_width(10)
        square.set_height(20)
        area = square.calculate_area()
        self.assertNotEqual(200, area)
        self.assertEqual(400, area)


if __name__ == '__main__':
    unittest.main()
