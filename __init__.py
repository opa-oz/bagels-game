from os import name, system
from constants import WELCOME_STRING, ONBOARDING_STRING, RULES_STRING


# Clean previous console input/output
def clean():
    # for windows
    if name == 'nt':
        system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')
    print('Tic-tac Toe!')


def welcome():
    print(WELCOME_STRING)


def on_boarding():
    print(ONBOARDING_STRING)


def rules():
    print(RULES_STRING)


def main():
    welcome()
    on_boarding()
    rules()


main()
