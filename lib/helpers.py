import os, math

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

DEFAULT_BOARD = [1, 2, 3, 4, 5, 6, 7, 8, 9]
PLAYER_ONE = "one"
PLAYER_TWO = "two"
BOARD_SPACE = "---+---+---\n"
PASS_AND_PLAY = "pap"
PLAYER_VS_COMPUTER = "pvsc"
POSITIVE_INFINITY = math.inf
NEGATIVE_INFINITY = -math.inf

class scores:
    X   =  1
    O   = -1
    TIE =  0

class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'