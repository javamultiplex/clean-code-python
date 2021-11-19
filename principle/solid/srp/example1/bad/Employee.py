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

    def isPromotionDueThisYear(self):
        # TODO: promotion logic implementation
        pass

    def calcIncomeTaxForCurrentYear(self):
        # TODO: income tax logic implementation
        pass


if __name__ == '__main__':
    e = Employee(123, "Rohit", "Rudrapur")
    print(e.address)
    print(e.id)
    print(e.name)