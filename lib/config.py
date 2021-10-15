import random, sys
from lib.helpers import clear, bcolors, PLAYER_ONE, PLAYER_TWO, PASS_AND_PLAY, PLAYER_VS_COMPUTER

get_mode = lambda: input(f"Select game mode: \n"
                          f"- [1] Pass-And-Play \n"
                          f"- [2] Player vs Computer \n"
                          f"Enter number[1/2]: ")

class Config:
  def __init__(self):
    pass

  def greetings(self):
    try:
      import pyfiglet
      print(pyfiglet.figlet_format("Tic Tac Toe", font = "digital" ))
    except:
      print(f"+-+-+-+ +-+-+-+ +-+-+-+\n"
            f"|T|i|c| |T|a|c| |T|o|e|\n"
            f"+-+-+-+ +-+-+-+ +-+-+-+\n")

  def info(self):
    print(f"Version: 0.0.1 \n"
          f"Github: https://github.com/rubix-lab/tic-tac-toe \n"
          f"Authors: IP99D & heitzlki \n")
    pass

  def _check_mode_config_input(self, mode_input):
    mode_input = mode_input.rstrip("\n")

    if(mode_input.isdigit() and int(mode_input) == 1):
      return PASS_AND_PLAY
    elif(mode_input.isdigit() and int(mode_input) == 2):
      return PLAYER_VS_COMPUTER
    else:
      return None
    
  
  def mode_config(self):
    mode_input = get_mode()
    mode_val = self._check_mode_config_input(mode_input)
    if(mode_val == None):
      return self.mode_config()
    else:
      self.mode = mode_val
      return self.mode

  def get_beginner(self):
    self.beginner = PLAYER_ONE if random.randint(0, 1) else PLAYER_TWO
    return self.beginner
  
  def _check_start_input(self, value):
    value = value.rstrip("\n")

    if(value == "j" or value == "J" or value == "y" or value == "Y"):
      return True
    elif(value == "n" or value == "N"):
      return False
    else:
      return None

  def start(self):
    start_value = input("Start game [y/N]: ")
    tmp_start = self._check_start_input(start_value)
    if(tmp_start == None):
      return self.start()
    else:
      return None if tmp_start == True else sys.exit()
  
  def config_info(self):
    str_mode = 'Pass-And-Play' if self.mode == PASS_AND_PLAY else 'Player vs Computer'
    str_beginner = f'{bcolors.FAIL}Player 1{bcolors.ENDC}' if self.beginner == PLAYER_ONE else (f'{bcolors.OKGREEN}Player 2{bcolors.ENDC}' if self.mode == PASS_AND_PLAY else f'{bcolors.OKGREEN}Computer{bcolors.ENDC}')
    print(f"\nMode: {str_mode} \n"
          f"Fisrt player: {str_beginner}\n")
  
  def setup(self):
    self.greetings()
    self.info()
    self.mode_config()
    self.get_beginner()
    self.config_info()
    self.start()
    clear()
    return self

if __name__ == "__main__":
  pass