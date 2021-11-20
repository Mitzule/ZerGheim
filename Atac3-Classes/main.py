import random
class player:
    def __init__(self,name,hp,attack,stamina):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = stamina
    def get_stats(self):
        print(f"{self.name} : hp: {self.hp}, attack: {self.attack}, stamina: {self.stamina}")

def chose_player(player_in):
    if player_in == "Warrior":
        return Warrior
    elif player_in == "Mage":
        return Mage
    elif player_in == "Rogue":
        return Rogue
    elif player_in == "Paladin":
        return Paladin

Warrior=player("Warrior",100,10,10)
Mage=player("Mage",100,8,15)
Rogue=player("Rogue",100,12,8)
Paladin=player("Paladin",100,5,20)

print("avaible players are:")
Warrior.get_stats()
Mage.get_stats()
Rogue.get_stats()
Paladin.get_stats()

x=input("chose from avaible player:")
y=input("chose from avaible player:")
p1=chose_player(x)
p2=chose_player(y)

while p1.hp>0 and p2.hp>0:
    p2.hp-=p1.attack
    p1.hp-=p2.attack

if p1.hp>0:
    print(f"winner: {p1.name}")
else:
    print(f"winner: {p2.name}")










