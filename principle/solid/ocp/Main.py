from Size import Size
from Color import Color
from Product import Product

if __name__ == '__main__':
    p = Product("Mango", Color.GREEN, Size.LARGE)
    p.color = Color.RED
    print(p.color.name)
    print(p.size.name)
    print(p.name)
