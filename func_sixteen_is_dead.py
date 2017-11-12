__author__ = "6611082: Cedric Reuter, 6317302: Fabian Eichner"
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
    end_game = False
    while pointslist[player-1] < 16:
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
            end_game= True
            break

        if(pointslist[player-1] == 9):
            print("Sie haben 9 Punkte erreicht. Leider darf nicht mehr weitergewürfelt werden")
            break

        if(pointslist[player-1] == 10):
            print("Sie haben 10 Punkte erreicht, das heißt es muss noch einmal gewürfelt werden")
            time.sleep(3)
            pointslist[player - 1] = points_result(pointslist[player-1])
            #with the break here, the player has to roll exactly once more, right?
            #I don't know about the rule set, but I think the idea is to force the
            #player once more and then let him decide again about further dice rolls
    if (end_game):
        return 2
    if(pointslist[player-1] >= 16):
        print("Spieler " + str(player) + " hat die Punktzahlgrenze überschritten")
        return 0

    else:
        return 1




def sixteen_is_dead(players):
    global pointslist
    defloser = False
    pointslist = [0] * players
    for i in range(1,players+1):
        x = turn(i)
        if(x == 0):
            print("Spieler " + str(i) + " hat verloren")
            defloser = True
            break
        elif(x == 2):
            print("Sie haben das Spiel beendet")
            break
    print("Punkteliste: ")
    for x in range(1,len(pointslist)+1):
        print("Spieler " + str(x) + " hat " + str(pointslist[x-1]) + " Punkte erreicht" )
    min = 100
    minpos = 0
    minposlist = [minpos]
    if(not defloser):
        for x in range(1,len(pointslist)+1):
            if pointslist[x-1] < min:
                min = pointslist[x-1]
                minpos = x-1
                minposlist = [minpos]
            if pointslist[x-1] == min:
                minposlist.append(x-1)
        for x in range(1, len(minposlist)): #multiple losers
            print("Spieler " + str(minposlist[x] + 1) + " hat verloren")
    
    newgame = ""
    newgame = input("Möchten Sie ein neues Spiel beginnen? Geben Sie dazu y ein und drücken Sie Return.") #entered desired input

    if(newgame == "y"):
            menu()

def menu():
    playercount = (input("Bitte geben Sie eine beliebige Spieleranzahl > 0 ein: "))
      
    if playercount.isdigit()and playercount != '0': #added check for valid number
        playercount = int(playercount)
        sixteen_is_dead(playercount)

menu()




