"""
@File      : Employee.py
@Author    : Rohit Agarwal on 24/11/21 10:18 pm
@Copyright : https://github.com/javamultiplex
"""


class Employee:
    def __init__(self, id: int, name: str, address: str) -> None:
        self._id = id
        self._name = name
        self._address = address

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, new_id: int):
        self._id = new_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, new_address: str):
        self._address = new_address

    def is_promotion_due_this_year(self) -> bool:
        # TODO: promotion logic implementation
        return False

    def calculate_tax_for_current_year(self) -> bool:
        # TODO: income tax logic implementation
        return False


if __name__ == '__main__':
    e = Employee(123, "Rohit", "Rudrapur")
    print(e.address)
    print(e.id)
    print(e.name)
