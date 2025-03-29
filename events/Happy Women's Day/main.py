import pyfiglet

ORANGE = '\033[38;2;255;103;31m'
WHITE = '\033[38;2;255;255;255m'
GREEN = '\033[38;2;0;255;0m'
PINK = '\033[38;2;255;105;180m'
RESET = '\033[0m'

FONT = pyfiglet.figlet_format('Happy Women\'s Day', font='slant')

print(ORANGE + FONT + RESET)
