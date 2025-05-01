import random

class Character:
  def __init__(self, name, health, attack_power):
    self.name = name
    self.health = health
    self.attack_power = attack_power
    self.max_health = health
    self.evading = False  

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
      

# EvilWizard
class EvilWizard(Character):
  def __init__(self, name):
    super().__init__(name, health=150, attack_power=15)

  def regenerate(self):
    regen_amount = 10
    self.health += regen_amount
    if self.health > self.max_health:
      self.health = self.max_health
    print(f"{self.name} regenerates 5 health! Current health: {self.health}")