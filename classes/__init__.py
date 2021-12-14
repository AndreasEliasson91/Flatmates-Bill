from fpdf import FPDF


class Bill:
    """
    Contains data about a bill, such as its type, total amount, due date and time period.
    """
    def __init__(self, amount: int, bill_type: str, due_date: str, names_on_bill: str, time_period: str):
        self.amount = amount
        self.bill_type = bill_type
        self.due_date = due_date
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

    def pays(self, bill: Bill, second_flatmate):
        weight = self.days_stayed / (self.days_stayed + second_flatmate.days_stayed)
        return bill.amount * weight


# class FlatmateRegistry:
#     """
#     A registry containing all flatmates currently living in the house.
#     """
#     def __init__(self):
#         self.registry = []


class PDFReport:
    """
    Creates a PDF with data about the bill amount, affected flatmates and a time period.
    """
    def generate(self, fm1: Flatmate, fm2: Flatmate, bill: Bill):
        filename = f'./bills/{bill.bill_type.lower()}_{bill.time_period.replace(" ", "").lower()}.pdf'
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image(name='./files/house.png', w=50, h=50)

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt=f'{bill.bill_type} {bill.time_period}', border=0, align='C', ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=120, h=40, txt=f'Due date: {bill.due_date}', border=0)
        pdf.cell(w=120, h=40, txt=f'Total: ${bill.amount}', border=0, align='C', ln=1)

        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=f'{fm1.name} : ${round(fm1.pays(bill, fm2), 2)}', border=0, ln=1)
        pdf.cell(w=100, h=25, txt=f'{fm2.name} : ${round(fm2.pays(bill, fm1), 2)}', border=0, ln=1)

        pdf.output(filename)
