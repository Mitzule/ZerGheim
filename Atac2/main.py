import random
#1.create the list of avaible players
lista=[["Warrior",100,10,10], ["Mage",100,8,15], ["Rogue",100,12,8], ["Paladin",100,5,20]]
print("Players Avaible (Name/Hp/Atk/Stamina): ",lista)
#stamina will count as chance of critical hits
#2.chose two player from the list avaible, and create another two list including their stats
first=int(input("Chose the player from 0 to 3: "))
second=int(input("Chose the player from 0 to 3: "))
player1=lista[first] #remember the statistics for player1
player2=lista[second] #and player2
print("Fight between player:",player1[0],"and player:",player2[0])
#3.HEAD OR TAIL
#a flip the coin ideea (if odd number starts first(head), if even starts second(tails))
#Head is 1, Tails is 2
HoT=random.randint(1,2)
hot=input("Head or Tails?")
if HoT==1:
    print("It was Head")
else:
    print("It was Tails")
#4.create stamina for critical hits
stp1=player1[3]#stamina player1
stp2=player2[3]#stamina player2
#5.Depending on HoT make the first move
#6.Also implement the critical hit in atack
if HoT%2==1:
#7.fight for the first player
    print(player1[0],"Starts first")
    while player1[1]>0 and player2[1]>0:
        CritHit=random.randint(1,30)#based on crithit, if is higher than stamina, you miss
        if CritHit<stp1 and CritHit<stp2:#both hit crit hit
            player2[1]-=player1[1]*2
            player1[1] -= player2[1] * 2
        if CritHit<stp1 and CritHit>stp2:#player1 crit hit, player2 miss
            player2[1] -= player1[1] * 2
            player1[1] -= player2[1]
        if CritHit>stp1 and CritHit<stp2:#player 1 miss, player 2 crit hit
            player2[1] -= player1[1]
            player1[1] -= player2[1] * 2
        if CritHit>stp1 and CritHit>stp2:#both miss
            player2[1] -= player1[1]
            player1[1] -= player2[1]
    if player1[1] > player2[1]:
        print("Winner is:", player1[0])
    else:
        print("Winner is:", player2[0])
else:
#8.fight for the second player
    print(player2[0],"Starts first")
    while player1[1] > 0 and player2[1] > 0:
        CritHit = random.randint(1, 30)  # based on crithit, if is higher than stamina, you miss
        if CritHit < stp1 and CritHit < stp2:  # both hit crit hit
            player1[1] -= player2[1] * 2
            player2[1] -= player1[1] * 2
        if CritHit < stp1 and CritHit > stp2:  # player1 crit hit, player2 miss
            player1[1] -= player2[1] * 2
            player2[1] -= player1[1]
        if CritHit > stp1 and CritHit < stp2:  # player 1 miss, player 2 crit hit
            player1[1] -= player2[1]
            player2[1] -= player1[1] * 2
        if CritHit > stp1 and CritHit > stp2:  # both miss
            player1[1] -= player2[1]
            player2[1] -= player1[1]
    if player1[1] > player2[1]:
        print("Winner is:", player1[0])
    else:
        print("Winner is:", player2[0])
