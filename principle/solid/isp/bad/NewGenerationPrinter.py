from Machine import Machine
from principle.solid.isp.Document import Document

"""
@File      : NewGenerationPrinter.py   
@Author    : Rohit Agarwal on 25/11/21 11:30 pm
@Copyright : https://github.com/javamultiplex
"""


class NewGenerationPrinter(Machine):
    def print(self, document: Document) -> None:
        print("Print " + str(document))

    def scan(self, document: Document) -> None:
        print("Scan " + str(document))

    def fax(self, document: Document) -> None:
        print("Fax " + str(document))
