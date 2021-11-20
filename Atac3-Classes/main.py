import random
class player:
    def __init__(self,name,hp,attack,stamina):
        self.hp=hp
        self.attack=attack
        self.stamina=stamina
        self.name=name
    def get_stats(self):
        print(f"{self.name} : hp: {self.hp}, attack: {self.attack}, stamina: {self.stamina}")

Warrior=player("Warrior",100,10,10)
Mage=player("Mage",100,8,15)
Rogue=player("Rogue",100,12,8)
Paladin=player("Paladin",100,5,20)
print("players list:")
Warrior.get_stats()
Mage.get_stats()
Rogue.get_stats()
Paladin.get_stats()




