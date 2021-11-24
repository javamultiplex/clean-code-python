from Size import Size
from Color import Color
from Product import Product

"""
@File      : Main.py   
@Author    : Rohit Agarwal on 24/11/21 10:18 pm
@Copyright : https://github.com/javamultiplex
"""

if __name__ == '__main__':
    p = Product("Mango", Color.GREEN, Size.LARGE)
    p.color = Color.RED
    print(p.color.name)
    print(p.size.name)
    print(p.name)
