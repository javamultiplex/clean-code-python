class Employee:
    def __init__(self, id, name, address):
        self._id = id
        self._name = name
        self._address = address

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, newId):
        self._id = newId

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name = newName

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, newAddress):
        self._address = newAddress


if __name__ == '__main__':
    employee = Employee(101, "Rohit", "Rudrapur")
    employee.id = 102
    employee.name = "Ram"
    print(employee.id)
    print(employee.name)
    print(employee.address)