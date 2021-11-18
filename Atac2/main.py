lista=[["warrior",100,10,10], ["mage",100,8,15], ["rogue",100,12,8], ["paladin",100,5,20]]
print("Players Avaible (Name/Hp/Atk/Stamina): ",lista)
first=int(input("Chose the player from 0 to 3: "))
second=int(input("Chose the player from 0 to 3: "))
player1=lista[first]
player2=lista[second]
print("First Fight between player:",player1[0],"and player:",player2[0])
#player from listB starts first
while player1[1]>0 and player2[1]>0:
    player1[1]-=player2[2]
    player2[1]-=player1[2]
if player1[1]>player2[1]:
    print("Winner is:",player1[0])
else:
    print("Winner is:",player2[0])
