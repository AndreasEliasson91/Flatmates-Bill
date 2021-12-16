from fpdf import FPDF
from models import Flatmate, Bill


class PDFReport:
    """
    Creates a PDF with data about the bill amount, affected flatmates and a time period.
    """
    @staticmethod
    def generate(fm1: Flatmate, fm2: Flatmate, bill: Bill):
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
        pdf.cell(w=100, h=25, txt=f'{fm1.name} : ${fm1.pays(bill, fm2)}', border=0, ln=1)
        pdf.cell(w=100, h=25, txt=f'{fm2.name} : ${fm2.pays(bill, fm1)}', border=0, ln=1)

        pdf.output(filename)