player1=100
player2=100
atack1=1
atack2=1
#player2 ataca primul, de aceea vom scadea prima data din viata player1
while player1>0 or player2>0:
    player1-=atack2
    player2-=atack1
#desi la final ambii sunt pe "minus" cu viata, diferenta se face pentru cel care are viata mai "mare"
if player1>player2:
    print("winner is: player1")
else:
    print("Winner is: player2")
#TO DO: improve critical hit, based on stamina