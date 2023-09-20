import csv

from PyInquirer import prompt

from expense import get_user

paid_option = {
    "type": "list",
    "name": "paid",
    "message": "Mark debt as indebted",
    "choices": ["Yes", "No"]
}

def get_expense():
    with open("expense_report.csv", 'r') as file:
        csvreader = csv.reader(file)

        return [val for val in csvreader]

def show_status(*args):
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    expenses = get_expense()
    debts = {}
    users = get_user()
    for user in users:
        debts[user] = {}
    print(debts)

    for expense in expenses:
        paybacks = expense[3].split("-")
        debt = float(expense[0]) / float(len(paybacks))
        for payback in paybacks:
            if not payback:
                continue
            if not expense[2] in debts[payback]:
                debts[payback][expense[2]] = debt
            else:
                debts[payback][expense[2]] += debt
    print(debts)