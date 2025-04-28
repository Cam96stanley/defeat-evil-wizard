import random
import time
import sys

# Base Character class
class Character:
  def __init__(self, name, health, attack_power):
    self.name = name
    self.health = health
    self.attack_power = attack_power
    self.max_health = health  

  def attack(self, opponent):
    if hasattr(opponent, 'evading') and opponent.evading:
      print(f"{opponent.name} evaded the attack!")
      opponent.evading = False
    else:
      min_damage = int(self.attack_power * 0.8)
      max_damage = int(self.attack_power * 1.2)
      damage = random.randint(min_damage, max_damage)
      opponent.health -= damage
      print(f"{self.name} attacks {opponent.name} for {damage} damage!")

  def display_stats(self):
    print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
    
  def heal(self):
    heal_amount = 20
    if self.health < self.max_health:
      self.health += heal_amount
      if self.health > self.max_health:
        self.health = self.max_health
      print(f"{self.name} healed {heal_amount} health. Current health: {self.health}/{self.max_health}")
    else:
      print(f"{self.name} is already at full health")
      

# EvilWizard class
class EvilWizard(Character):
  def __init__(self, name):
    super().__init__(name, health=150, attack_power=15)

  def regenerate(self):
    regen_amount = 10
    self.health += regen_amount
    if self.health > self.max_health:
      self.health = self.max_health
    print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
# Warrior class
class Warrior(Character):
  def __init__(self, name):
    super().__init__(name, health=140, attack_power=25)
           
# Mage class
class Mage(Character):
  def __init__(self, name):
    super().__init__(name, health=100, attack_power=35)

# Archer class
class Archer(Character):
  def __init__(self, name):
    super().__init__(name, health=100, attack_power=15)
    self.evading = False
      
  def quick_shot(self, opponent):
    self.attack_power *= 2
    print(f"{self.name} used Quick Shot!")
    self.attack(opponent)
    self.attack_power //= 2
    
  def evade(self):
    self.evading = True
    print(f"{self.name} is preparing to evade the next attack!")
  

# Paladin class 
class Paladin(Character):
  def __init__(self, name):
    super().__init__(name, health=160, attack_power=10)
    self.evading = False
  
  def holy_strike(self, opponent):
    self.attack_power *= 2
    print(f"{self.name} used Holy Strike!")
    self.attack(opponent)
    self.attack_power //= 2

  def divine_shield(self):
    self.evading = True
    print(f"{self.name} is protected against the next attack using Divine Shield!")
    
# user-interface logic
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

def main():
  player = create_character()
  wizard = EvilWizard("The Dark Wizard")
  battle(player, wizard)

if __name__ == "__main__":
  main()
