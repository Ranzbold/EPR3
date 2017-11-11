__author__ = "6611082: Cedric Reuter"
import func_roll_dice
import time
global pointslist



def points_result(pts):
    pts = int(pts)
    result = int(func_roll_dice.roll_dice(1, 6, None))
    print("Sie haben eine " + str(result) + " gewürfelt")
    ptsresult = pts + result
    print("Sie haben nun: " + str(ptsresult) + " Punkte")
    return ptsresult

def turn(player):
    while pointslist[0] < 16:
        print("Spieler " + str(player) + " ist am Zug")
        print("Drücken sie Return um erneut zu würfeln.")
        print("Drücken sie n um den Knobelbecher weiterzurreichen")
        print("Drücken sie x um das Spiel jederzeit zu beenden")
        usrinput = input("-->")
        if(usrinput == "n"):
            break
        elif(usrinput == ""):

            pointslist[player - 1] = points_result(pointslist[player-1])
        elif(usrinput == "x"):
            pass

        if(pointslist[player-1] == 9):
            print("Sie haben 9 Punkte erreicht. Leider darf nicht mehr weitergewürfelt werden")
            break

        if(pointslist[player-1] == 10):
            print("Sie haben 10 Punkte erreicht, das heißt es muss noch einmal gewürfelt werden")
            time.sleep(3)
            pointslist[player - 1] = points_result(pointslist[player-1])
    if(pointslist[player-1] >= 16):
        print(pointslist[player-1])
        print("Spieler " + str(player) + " hat die Punktzahlgrenze überschritten")
        return False
    else:
        return True




def sixteen_is_dead(players):
    global pointslist
    defloser = False
    pointslist = [0] * players
    for i in range(1,players+1):
        if(not turn(i)):
            print("Spieler " + str(i) + " hat verloren")
            defloser = True
            break
    print("Punkteliste: ")
    for x in range(1,len(pointslist)+1):
        print("Spieler " + str(x) + " hat " + str(pointslist[x-1]) + " Punkte erreicht" )
    min = 100
    minpos = 0
    if(not defloser):
        for x in range(1,len(pointslist)+1):
            if pointslist[x-1] < min:
                min = pointslist[x-1]
                minpos = x-1
        print("Spieler " + str(minpos + 1) + " hat verloren")





sixteen_is_dead(2)










