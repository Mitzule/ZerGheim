lista=[["player1",100,10], ["player2",100,8], ["player3",100,12], ["player2",100,5]]
print("Players Avaible (Name/Hp/Atk): ",lista)
a=int(input("Chose the player from 0 to 3: "))
b=int(input("Chose the player from 0 to 3: "))
print("First Fight between player",a+1,"and player",b+1)
listaA=lista[a]
listaB=lista[b]
#player from listB starts first
while listaA[1]>0 and listaB[1]>0:
    listaA[1]-=listaB[2]
    listaB[1]-=listaA[2]
if listaA[1]>listaB[1]:
    print("Winner is:",listaA[0])
else:
    print("Winner is:",listaB[0])
