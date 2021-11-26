from Fax import Fax
from Printer import Printer
from Scanner import Scanner
from principle.solid.isp.Document import Document

"""
@File      : NewGenerationPrinter.py   
@Author    : Rohit Agarwal on 26/11/21 9:40 pm
@Copyright : https://github.com/javamultiplex
"""


class NewGenerationPrinter(Printer, Scanner, Fax):
    def print(self, document: Document) -> None:
        print("Print " + str(document))

    def scan(self, document: Document) -> None:
        print("Scan " + str(document))

    def fax(self, document: Document) -> None:
        print("Fax " + str(document))
