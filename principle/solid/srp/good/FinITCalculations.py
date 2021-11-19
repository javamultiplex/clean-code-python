from Employee import Employee


class FinITCalculations:
    def calcIncomeTaxForCurrentYear(self, employee):
        # TODO: Tax calculation logic
        pass


if __name__ == '__main__':
    obj = FinITCalculations()
    e = Employee(101, "Rohit", "Delhi")
    obj.calcIncomeTaxForCurrentYear(e)
