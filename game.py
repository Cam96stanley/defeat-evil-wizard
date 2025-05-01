import sys
import time
from classes import Warrior, Mage, Archer, Paladin

def create_character():
  print("Choose your character class:")
  print("1. Warrior")
  print("2. Mage")
  print("3. Archer") 
  print("4. Paladin")  

  class_choice = input("Enter the number of your class choice: ")
  name = input("Enter your character's name: ")

  if class_choice == '1':
      return Warrior(name)
  elif class_choice == '2':
      return Mage(name)
  elif class_choice == '3':
      return Archer(name)
  elif class_choice == '4':
      return Paladin(name)
  else:
      print("Invalid choice. Defaulting to Warrior.")
      return Warrior(name)

def battle(player, wizard):
  while wizard.health > 0 and player.health > 0:
    print("\n--- Your Turn ---")
    print("1. Attack")
    print("2. Use Special Ability")
    print("3. Heal")
    print("4. View Stats")

    choice = input("Choose an action: ")

    if choice == '1':
      player.attack(wizard)
    elif choice == '2':
      if isinstance(player, Archer):
        print("1. Quick Shot\n2. Evade")
        special = input("Choose an ability: ")
        if special == '1':
          player.quick_shot(wizard)
        elif special == '2':
          player.evade()
        else:
          print("Invalid choice. Please enter 1 or 2")
      elif isinstance(player, Paladin):
        print("1. Holy Strike\n2. Divine Shield")
        special = input("Choose an ability: ")
        if special == '1':
          player.holy_strike(wizard)
        elif special == '2':
          player.divine_shield()
        else:
          print("Invalid choice. Please enter 1 or 2")
      elif isinstance(player, Mage):
        print("1. Fire Ball\n2. Mana Shield")
        special = input("Choose an ability: ")
        if special == '1':
          player.fire_ball(wizard)
        elif special == '2':
          player.mana_shield()
        else:
          print("Invalid choice. Please enter 1 or 2")
      elif isinstance(player, Warrior):
        print("1. Berserker Strike\n2. Almighty Shield")
        special = input("Choose an ability: ")
        if special == '1':
          player.berserker_strike(wizard)
        elif special == '2':
          player.almighty_shield()
        else:
          print("Invalid choice. Please enter 1 or 2")
      else:
        print("This class has no special abilites yet.")
    elif choice == '3':
      player.heal()
    elif choice == '4':
      player.display_stats()
    else:
      print("Invalid choice. Try again.")

    if wizard.health > 0:
      wizard.regenerate()
      wizard.attack(player)

    if player.health <= 0:
      slow_print(f"{player.name} has been defeated...", delay=0.1)
      slow_print("The Dark Wizard stands victorious. The realm falls into shadow...", delay=0.05)
      break

    if wizard.health <= 0:
      slow_print(f"The Dark Wizard has been defeated by {player.name}!", delay=0.1)
      slow_print("Light returns to the land. You are victorious!", delay=0.05)
      break
    
def slow_print(text, delay=0.05):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()