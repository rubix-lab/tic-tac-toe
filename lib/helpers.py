import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

PLAYER_ONE = "first"
PLAYER_TWO = "second"
BOARD_SPACE = "---+---+---\n"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'