import models as m
from models import pdf


def main():
    name1 = input('Enter your name:\n>> ')
    days1 = int(input('How many days did you stay in the apartment?\n>> '))

    bill_type = input('What type of bill is it?\n>> ')
    amount = float(input('Enter the amount:\n>> '))
    due_date = input('Enter the bill due date:\n>> ')
    time_period = input('During what time period is the bill? E.g. December 2021\n>> ')

    name2 = input('What\'s your roommates name?\n>> ')
    days2 = int(input(f'How many days did {name2} stay in the apartment?\n>> '))

    p1 = m.Flatmate(name1, days1)
    p2 = m.Flatmate(name2, days2)
    bill = m.Bill(amount, bill_type, due_date, time_period)
    pdf.PDFReport.generate(p1, p2, bill)


if __name__ == '__main__':
    main()
