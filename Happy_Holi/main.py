import pyfiglet
from termcolor import colored


def wish_happy_holi():
    holi_message = pyfiglet.figlet_format("Happy Holi")
    colored_message = colored(holi_message, 'red', attrs=['bold'])
    print(colored_message)

    print(colored("May your life be filled with vibrant colors and joy!", 'yellow'))
    print(colored("Wishing you a colorful and joyous Holi!", 'green'))

wish_happy_holi()

