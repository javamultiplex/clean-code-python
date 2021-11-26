import traceback
import unittest

from NewGenerationPrinter import NewGenerationPrinter
from OldGenerationPrinter import OldGenerationPrinter
from UnsupportedOperationError import UnsupportedOperationError
from principle.solid.isp.Document import Document


class Tests(unittest.TestCase):

    def test_new_generation_printer(self):
        new_generation_printer = NewGenerationPrinter()
        document = Document()
        document.name = "image"
        document.size = 10
        new_generation_printer.print(document)
        new_generation_printer.scan(document)
        new_generation_printer.fax(document)

    def test_old_generation_printer(self):
        new_generation_printer = OldGenerationPrinter()
        document = Document()
        document.name = "image"
        document.size = 10
        new_generation_printer.print(document)
        try:
            new_generation_printer.scan(document)
        except UnsupportedOperationError as ex:
            print(ex)
            traceback.print_exc()

        try:
            new_generation_printer.fax(document)
        except UnsupportedOperationError as ex:
            print(ex)
            traceback.print_exc()


if __name__ == '__main__':
    unittest.main()
