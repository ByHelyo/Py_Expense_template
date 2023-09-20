from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    }
]


def get_user():
    with open("users.csv", 'r') as file:
        csvreader = csv.reader(file)

        return [val[0] for val in csvreader]


def user_question(users):
    return {
        "type": "list",
        "name": "user",
        "message": "Choose spender",
        "choices": users
    }


def payback_question(users):
    return {
        "type": "list",
        "name": "user",
        "message": "Choose payback",
        "choices": users
    }


def new_expense(*args):
    infos = prompt(expense_questions)
    users = get_user()
    choosen_user = prompt(user_question(users))
    infos["spender"] = choosen_user["user"]
    paybacks = []
    users.remove(infos["spender"])
    users.append("Stop")

    while True:
        choosen_payback = prompt(payback_question(users))
        if choosen_payback["user"] == "Stop":
            break
        users.remove(choosen_payback["user"])
        paybacks.append(choosen_payback["user"])

    infos["payback"] = "-".join(paybacks)

    with open('expense_report.csv', mode='a') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow([val for val in infos.values()])

    print("Expense Added !")
    return True
