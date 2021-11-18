lista=[["Warrior",100,10,10], ["Mage",100,8,15], ["Rogue",100,12,8], ["Paladin",100,5,20]]
print("Players Avaible (Name/Hp/Atk/Stamina): ",lista)
#stamina will count as chance of critical hits
first=int(input("Chose the player from 0 to 3: "))
second=int(input("Chose the player from 0 to 3: "))
player1=lista[first] #remeber the statistics for player1
player2=lista[second] #and player2
print("Fight between player:",player1[0],"and player:",player2[0])
#who starts first ?
#a flip the coin ideea (if odd number starts first(head), if even starts second(tails))
HoT=int(input("Head or Tails? Chose a number from 1 and 2"))
if HoT%2==1:
#fight for the first player
    print(player1[0],"Starts first")
    while player1[1]>0 and player2[1]>0:
        player2[1] -= player1[2]
        player1[1] -= player2[2]
    if player1[1] > player2[1]:
        print("Winner is:", player1[0])
    else:
        print("Winner is:", player2[0])
else:
#fight for the second player
    print(player2[0],"Starts first")
    while player1[1] > 0 and player2[1] > 0:
        player1[1] -= player2[2]
        player2[1] -= player1[2]
    if player1[1] > player2[1]:
        print("Winner is:", player1[0])
    else:
        print("Winner is:", player2[0])
