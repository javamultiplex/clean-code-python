from Employee import Employee


class FinITCalculations:
    def calcIncomeTaxForCurrentYear(self, employee: Employee) -> bool:
        # TODO: Tax calculation logic
        print(employee)
        return False


if __name__ == '__main__':
    obj = FinITCalculations()
    e = Employee(102, "Rohit", "Delhi")
    obj.calcIncomeTaxForCurrentYear(e)
