import classes as c


def main():
    p1 = c.Flatmate('John', 20)
    p2 = c.Flatmate('Mary', 25)
    bill = c.Bill(120, 'Rent', '2021-10-28', ' ', 'September 2021')
    pdf_report = c.PDFReport()
    pdf_report.generate(p1, p2, bill)


if __name__ == '__main__':
    main()
