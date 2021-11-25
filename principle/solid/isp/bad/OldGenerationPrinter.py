from Machine import Machine
from principle.solid.isp.Document import Document

"""
@File      : OldGenerationPrinter.py   
@Author    : Rohit Agarwal on 25/11/21 11:31 pm
@Copyright : https://github.com/javamultiplex
"""


class OldGenerationPrinter(Machine):

    def print(self, document: Document) -> None:
        print("Print " + str(document))

    def scan(self, document: Document) -> None:
        raise RuntimeError("scan not supported")

    def fax(self, document: Document) -> None:
        raise RuntimeError("fax not supported")
