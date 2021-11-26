from Printer import Printer
from principle.solid.isp.Document import Document

"""
@File      : OldGenerationPrinter.py   
@Author    : Rohit Agarwal on 26/11/21 9:42 pm
@Copyright : https://github.com/javamultiplex
"""


class OldGenerationPrinter(Printer):
    def print(self, document: Document) -> None:
        print("Print " + str(document))
