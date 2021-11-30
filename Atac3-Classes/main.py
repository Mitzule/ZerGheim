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
        hot=input("Head or Tails? ")
        if HoT==1:
            print("It was Head, you start first ")
        else:
            print("It was Tails, enemy starts first")
        i=1
        print()
        if HoT%2==1:
            while self.hp>0 and self1.hp>0:
                CritHit=random.randint(1,30)
                if CritHit<self.crit and CritHit<self1.crit:
                    self1.hp-= self.atac * 2
                    print(i,". ",self.name, "attacked", self1.name, "for", self.atac * 2, "damage")
                    self.hp -= self1.atac * 2
                    print(i, ". ", self1.name, "attacked", self.name, "for", self1.atac * 2, "damage")
                if CritHit<self.crit and CritHit>self1.crit:
                    self1.hp-= self.atac * 2
                    print(i,". ",self.name, "attacked", self1.name, "for", self.atac * 2, "damage")
                    self.hp -= self1.atac
                    print(i, ". ", self1.name, "attacked", self.name, "for", self1.atac, "damage")
                if CritHit>self.crit and CritHit<self1.crit:
                    self1.hp-= self.atac
                    print(i,". ",self.name, "attacked", self1.name, "for", self.atac, "damage")
                    self.hp -= self1.atac * 2
                    print(i, ". ", self1.name, "attacked", self.name, "for", self1.atac * 2, "damage")
                if CritHit>self.crit and CritHit>self1.crit:
                    self1.hp-= self.atac
                    print(i,". ",self.name, "attacked", self1.name, "for", self.atac, "damage")
                    self.hp -= self1.atac
                    print(i, ". ", self1.name, "attacked", self.name, "for", self1.atac, "damage")
                print(i, ". ", self.name, "hp left: ", self.hp, "---", self1.name, "hp left: ", self1.hp)
                i+=1
                print()
            if self.hp > self1.hp:
                print("Winner is:", self.name)
            else:
                print("Winner is:", self1.name)
        else:
            while self.hp > 0 and self1.hp > 0:
                CritHit = random.randint(1, 30)
                if CritHit < self.crit and CritHit < self1.crit:
                    self.hp -= self1.atac * 2
                    print(i, ". ", self1.name, "attacked", self.name, "for", self1.atac * 2, "damage")
                    self1.hp -= self.atac * 2
                    print(i,". ",self.name, "attacked", self1.name, "for", self.atac * 2, "damage")
                if CritHit < self.crit and CritHit > self1.crit:
                     self.hp -= self1.atac * 2
                     print(i, ". ", self1.name, "attacked", self.name, "for", self1.atac * 2, "damage")
                     self1.hp -= self.atac
                     print(i,". ",self.name, "attacked", self1.name, "for", self.atac, "damage")
                if CritHit > self.crit and CritHit < self1.crit:
                     self.hp -= self1.atac
                     print(i, ". ", self1.name, "attacked", self.name, "for", self1.atac, "damage")
                     self1.hp -= self.atac * 2
                     print(i,". ",self.name, "attacked", self1.name, "for", self.atac * 2, "damage")
                if CritHit > self.crit and CritHit > self1.crit:
                     self.hp -= self1.atac
                     print(i, ". ", self1.name, "attacked", self.name, "for", self1.atac, "damage")
                     self1.hp -= self.atac
                     print(i,". ",self.name, "attacked", self1.name, "for", self.atac, "damage")
                print(i, ". ", self.name, "hp left: ", self.hp, "---", self1.name, "hp left: ", self1.hp)
                i+=1
                print()
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
print("=======================================================================")
print("=                                                                     =")
print("= Avaible players: Warrior, Mage, Rogue, Paladin. Chose two (w/m/r/p) =")
print("=                                                                     =")
print("=======================================================================")
x=input("You chose: ")
y=input("Enemy chose: ")
p1=order(x)
p2=order(y)
p1.fight(p2)
#print(16-((30/100)*16)) armor represents atac-(arm/100)%*atac