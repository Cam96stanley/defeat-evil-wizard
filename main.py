from game import create_character, battle
from character import EvilWizard

def main():
  player = create_character()
  wizard = EvilWizard("The Dark Wizard")
  battle(player, wizard)

if __name__ == "__main__":
  main()
