from Employee import Employee

"""
@File      : FinITCalculations.py   
@Author    : Rohit Agarwal on 24/11/21 10:18 pm
@Copyright : https://github.com/javamultiplex
"""


class FinITCalculations:
    def calcIncomeTaxForCurrentYear(self, employee: Employee) -> bool:
        # TODO: Tax calculation logic
        print(employee)
        return False


if __name__ == '__main__':
    obj = FinITCalculations()
    e = Employee(102, "Rohit", "Delhi")
    obj.calcIncomeTaxForCurrentYear(e)
