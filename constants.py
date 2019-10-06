from bcolors import BColors

DIGITS_COUNT = 3

MAX_GUESS_COUNT = 10

WELCOME_STRING = '''
    ===========================
    🥯 Welcome to {b}{green}the {un}Bagels{end} 🥯
    ===========================
'''.format(
    end=BColors.ENDC,
    b=BColors.BOLD,
    un=BColors.UNDERLINE,
    green=BColors.OKGREEN,
)

RULES_STRING = '''
    {h}{b}{un}Rules:{end}
    \t - Computer thinks up a random {blue}{dg}-digit{end} number with no repeating digits, and you try to guess what the number is.
    \t - After each guess, computer gives you {un}three types{end} of clues:
    \t\t # {b}{green}Bagels{end} 
    \t\t\t  – {b}None{end} of the three digits you guessed is in the secret number.
    \t\t # {b}{green}Pico{end} 
    \t\t\t  – {b}One{end} of the digits is in the secret number, but your guess has the digit in the {un}wrong place{end}.
    \t\t # {b}{green}Fermi{end}  
    \t\t\t  – Your guess has a {b}correct digit{end} in the {b}correct place{end}.
    \t - You {un}can{end} get {blue}multiple{end} clues after each guess.
    \t - {red}[Important]{end} You have only {blue}{b}{gc}{end} tries.
    \n
    {h}{b}{un}Example:{end}
    \t 1. The secret number is: {blue}{b}456{end};
    \t 2. Your guess is: {blue}{b}546{end};
    \t 3. Computer's output would be: {blue}"fermi pico pico"{end}; 
    \t 4. The {blue}{b}6{end} provides {b}{green}"fermi"{end} ;
    \t 5. The {blue}{b}5{end} and {blue}{b}4{end} provide {b}{green}"pico pico"{end}.
'''.format(
    dg=DIGITS_COUNT,
    gc=MAX_GUESS_COUNT,
    h=BColors.HEADER,
    end=BColors.ENDC,
    b=BColors.BOLD,
    un=BColors.UNDERLINE,
    green=BColors.OKGREEN,
    blue=BColors.OKBLUE,
    red=BColors.FAIL
)

ONBOARDING_STRING = '''
    Use {b}{h}"rules"{end} to see the rules
'''.format(
    h=BColors.HEADER,
    end=BColors.ENDC,
    b=BColors.BOLD,
)
