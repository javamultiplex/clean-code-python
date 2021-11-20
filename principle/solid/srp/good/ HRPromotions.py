from Employee import Employee


class HRPromotions:
    def is_promotion_due_this_year(self, employee: Employee) -> bool:
        # TODO: Promotion logic
        print(employee)
        return False


if __name__ == '__main__':
    obj = HRPromotions()
    e = Employee(123, "Rohit", "Delhi")
    obj.is_promotion_due_this_year(e)
