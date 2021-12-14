class Bill:
    """
    Contains data about a bill, such as its type, total amount, due date and time period.
    """
    def __init__(self, amount: int, bill_type: str, due_date: str, names_on_bill: str, time_period: str):
        self.amount = amount
        # self.bill_type = bill_type
        # self.due_date = due_date
        # self.names_on_bill = names_on_bill.split(' ')
        self.time_period = time_period


class Flatmate:
    """
    Creates a flatmate object.
    The flatmate pays it shares of the bills based on how many days they stayed in the house.
    """
    def __init__(self, name: str, days_stayed: int):
        self.name = name
        self.days_stayed = days_stayed

    def pays(self, bill: Bill, fm2):
        weight = self.days_stayed / (self.days_stayed + fm2.days_stayed)
        return bill.amount * weight


# class FlatmateRegistry:
#     """
#     A registry containing all flatmates currently living in the house.
#     """
#     def __init__(self):
#         self.registry = []


class ReportPDF:
    """
    Creates a PDF with data about the bill amount, affected flatmates and a time period.
    """
    def __init__(self, filename: str):
        self.filename = filename

    def generate(self, fm1: Flatmate, fm2: Flatmate, bill: Bill):
        pass
