from character import Character

# Warror class
class Warrior(Character):
  def __init__(self, name):
    super().__init__(name, health=140, attack_power=25)
    
  def berserker_strike(self, opponent):
    self.attack_power *= 2
    print(f"{self.name} used Berserker Strike!")
    self.attack(opponent)
    self.attack_power //= 2
    
  def almighty_shield(self):
    self.evading = True
    print(f"{self.name} has used Almighty Shield!")
    
           
# Mage class
class Mage(Character):
  def __init__(self, name):
    super().__init__(name, health=100, attack_power=35)
    
  def fire_ball(self, opponent):
    self.attack_power *= 3
    print(f"{self.name} used Fire Ball!")
    self.attack(opponent)
    self.attack_power //= 3
    
  def mana_shield(self):
    self.evading = True
    print(f"{self.name} has used Mana Shield!")

# Archer class
class Archer(Character):
  def __init__(self, name):
    super().__init__(name, health=100, attack_power=15)
      
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
  
  def holy_strike(self, opponent):
    self.attack_power *= 2
    print(f"{self.name} used Holy Strike!")
    self.attack(opponent)
    self.attack_power //= 2

  def divine_shield(self):
    self.evading = True
    print(f"{self.name} is protected against the next attack using Divine Shield!")