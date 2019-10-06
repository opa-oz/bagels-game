import random
from os import name, system
from constants import WELCOME_STRING, ONBOARDING_STRING, RULES_STRING, DIGITS_COUNT, Clues, MAX_GUESS_COUNT
from bcolors import BColors


# Clean previous console input/output
def clean():
    # for windows
    if name == 'nt':
        system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


def get_secret_number(length):
    numbers = list(range(10))
    random.shuffle(numbers)

    numbers = numbers[:length]
    numbers = map(lambda n: str(n), numbers)

    return ''.join(numbers)


def is_only_digits(guess):
    if guess == '':
        return False

    pattern = '123456789'
    result = True
    for value in list(guess):
        if value not in pattern:
            result = False

    return result


def is_unrepeated(guess, length):
    guess_list = list(guess)
    guess_set = set(guess_list)

    return len(guess_set) == length


def find_clues(guess, secret_num):
    if guess == secret_num:
        return True

    guess_list = list(guess)
    secret_num_list = list(secret_num)
    clues = []

    for number in guess_list:
        key = guess_list.index(number)
        if number in secret_num_list and secret_num_list.index(number) == key:
            clues.append(Clues.FERMI)
        elif number in secret_num_list:
            clues.append(Clues.PICO)

    if len(clues) == 0:
        clues.append(Clues.BAGELS)

    clues.sort()
    return clues


def input_guess(length, trying):
    print('  {b}Guess {blue}{t}{end}:'.format(
        t=trying,
        b=BColors.BOLD,
        blue=BColors.OKBLUE,
        end=BColors.ENDC
    ))
    guess = input()
    while not is_only_digits(guess) or len(guess) != length or not is_unrepeated(guess, length):
        if guess == 'rules':
            rules()
            guess = input()
            continue
        print('Wrong input! Please, use only digits {} times, without repeating'.format(length))
        guess = input()

    return guess


def welcome():
    print(WELCOME_STRING)


def on_boarding():
    print(ONBOARDING_STRING)


def rules():
    print(RULES_STRING)


def main():
    while True:
        clean()
        welcome()
        on_boarding()
        secret_num = get_secret_number(DIGITS_COUNT)
        guesses_count = 1
        print('So, I thought a {}-digits number. Try to guess!'.format(DIGITS_COUNT))
        while guesses_count <= MAX_GUESS_COUNT:
            guess = input_guess(DIGITS_COUNT, guesses_count)
            guesses_count += 1
            clues = find_clues(guess, secret_num)
            if clues == True:
                print('\tYou {b}{green}won!{end} Good job!'.format(
                    b=BColors.BOLD,
                    green=BColors.OKGREEN,
                    end=BColors.ENDC
                ))
                break
            print(' '.join(clues))
            if guesses_count == MAX_GUESS_COUNT + 1:
                print('You {b}{red}lose!{end} The secret number was {b}{number}{end}'.format(
                    b=BColors.BOLD,
                    red=BColors.OKGREEN,
                    end=BColors.ENDC,
                    number=secret_num
                ))
                break

        print('Would you like to play again? ({b}{green}yes/{red}no{end})'.format(
            red=BColors.FAIL,
            green=BColors.OKGREEN,
            b=BColors.BOLD,
            end=BColors.ENDC
        ))

        answer = input().lower()

        if answer not in ['yes', 'y']:
            break


main()
