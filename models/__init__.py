class Bill:
    """
    Contains data about a bill, such as its type, total amount, due date and time period.
    """
    def __init__(self, amount: float, bill_type: str, due_date: str, time_period: str):
        self.amount = amount
        self.bill_type = bill_type
        self.due_date = due_date
        self.time_period = time_period


class Flatmate:
    """
    Creates a flatmate object.
    The flatmate pays it shares of the bills based on how many days they stayed in the house.
    """
    def __init__(self, name: str, days_stayed: int):
        self.name = name
        self.days_stayed = days_stayed

    def pays(self, bill: Bill, second_flatmate) -> float:
        weight = self.days_stayed / (self.days_stayed + second_flatmate.days_stayed)
        return round((bill.amount * weight), 2)
