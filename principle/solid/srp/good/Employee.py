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

    def __str__(self) -> str:
        return " ".join([str(self.id), self.name, self.address])


if __name__ == '__main__':
    employee = Employee(101, "Rohit", "Rudrapur")
    employee.id = 102
    employee.name = "Ram"
    print(employee.id)
    print(employee.name)
    print(employee.address)
