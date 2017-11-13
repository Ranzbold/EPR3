__author__ = "6611082: Cedric Reuter, 6317302: Fabian Eichner"

"""In the following, the gameflow for the game sixteen_is_dead is presented.
This game lets the players' roll a dice and counts the results. The goal of the
game is to come as close to the cumulative count of 16 as possible. If the count
of 16 is reached or exceeded, however, the player loses. The following code is 
required for EPR_03, exercises 3.3c), 3.4 and 3.5."""

import func_roll_dice
import time
global pointslist



def points_result(pts):
    """points_result calls on func_dice_roll to execute a dice roll, prints out
    the result and returns the player's updated point count. Input argument has
    to be a list element containing an integer, output is an integer."""
    pts = int(pts)
    result = int(func_roll_dice.roll_dice(1, 6, None))
    print("Sie haben eine " + str(result) + " gewürfelt")
    ptsresult = pts + result
    print("Sie haben nun: " + str(ptsresult) + " Punkte")
    return ptsresult

def turn(player):
    """turn instructs the player and receives the player's input. The player has
    the choice to execute a dice roll (in which case points_result is called),
    pass over to the next player or end the game. turn also incorporates the
    exceptional rules that apply to the pointcount of 9 or 10 points. turn
    receives an input integer denoting the active player and returns an integer
    denoting the player's decision"""
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

    if (end_game):
        return 2
    
    if(pointslist[player-1] >= 16):
        print("Spieler " + str(player) + " hat die Punktzahlgrenze überschritten")
        return 0

    else:
        return 1




def sixteen_is_dead(players):
    """sixteen_is_dead sets up the list storing the players' points and calls
    turn to execute the players' turns. When the game ends, sixteen_is_dead
    prints out the players' point counts, determines the loser(s). Then it
    offers to start anew. sixteen_is_dead receives the number of players as
    input."""
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
        for x in range(1, len(minposlist)): 
            print("Spieler " + str(minposlist[x] + 1) + " hat verloren")
    
    newgame = ""
    newgame = input("Möchten Sie ein neues Spiel beginnen? Geben Sie dazu y ein und drücken Sie Return.") 

    if(newgame == "y"):
            menu()

def menu():
    """menu asks for the number of players and the initiates sixteen_is_dead to
    start the game."""
    playercount = (input("Bitte geben Sie eine beliebige Spieleranzahl > 0 ein: "))
      
    if playercount.isdigit()and playercount != '0': 
        playercount = int(playercount)
        sixteen_is_dead(playercount)

menu()




