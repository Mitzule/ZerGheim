import random
class player:
    def __init__(self,name, hp, atac, crit):
        self.name = name
        self.hp = hp
        self.atac = atac
        self.crit = crit

    def afis(self):
      print(self.name, self.hp, self.atac, self.crit)

    #fight
    def fight(self, self1):
        HoT=random.randint(1,2)
        hot=input("Head or Tails?")
        if HoT==1:
            print("It was Head")
        else:
            print("It was Tails")
        if HoT%2==1:
            print(self.name,"Starts first")
            while self.hp>0 and self1.hp>0:
                CritHit=random.randint(1,30)
                if CritHit<self.crit and CritHit<self1.crit:
                    self1.hp-= self.atac * 2
                    self.hp -= self1.atac * 2
                if CritHit<self.crit and CritHit>self1.crit:
                    self1.hp-= self.atac * 2
                    self.hp -= self1.atac
                if CritHit>self.crit and CritHit<self1.crit:
                    self1.hp-= self.atac
                    self.hp -= self1.atac * 2
                if CritHit>self.crit and CritHit>self1.crit:
                    self1.hp-= self.atac
                    self.hp -= self1.atac
            if self.hp > self1.hp:
                print("Winner is:", self.name)
            else:
                print("Winner is:", self1.name)
        else:
            print(self1.name,"Starts first")
            while self.hp > 0 and self1.hp > 0:
                CritHit = random.randint(1, 30)
                if CritHit < self.crit and CritHit < self1.crit:
                    self.hp -= self1.atac * 2
                    self1.hp -= self.atac * 2
                if CritHit < self.crit and CritHit > self1.crit:
                     self.hp -= self1.atac * 2
                     self1.hp -= self.atac
                if CritHit > self.crit and CritHit < self1.crit:
                     self.hp -= self1.atac
                     self1.hp -= self.atac * 2
                if CritHit > self.crit and CritHit > self1.crit:
                     self.hp -= self1.atac
                     self1.hp -= self.atac
            if self.hp > self1.hp:
                print("Winner is:", self.name)
            else:
                print("Winner is:", self1.name)

#player init
Warrior=player("Warrior", 100, 10, 10)
Mage=player("Mage", 100, 8, 15)
Rogue=player("Rogue", 100, 12, 8)
Paladin=player("Paladin", 100, 5, 20)

#player chose
def order(player_in):
    if player_in == "w":
        return Warrior
    elif player_in == "m":
        return Mage
    elif player_in == "r":
        return Rogue
    elif player_in == "p":
        return Paladin
print("Avaible players: Warrior, Mage, Rogue, Paladin")
x=input()
y=input()
p1=order(x)
p2=order(y)
p1.fight(p2)
