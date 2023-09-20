import csv

from PyInquirer import prompt

user_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New User - Name: ",
    }
]

def add_user(*args):
    infos = prompt(user_questions)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('users.csv', mode='a') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow([val for val in infos.values()])

    print("User Added !")
    return True
