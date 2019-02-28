game = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]

def main():
    
    print("This is the TicTacToe app.")
    print("This is a tictactoe game. First player is cross and second is circle. \n You enter first the row and then the column of where you want to place your symbol. \n Continue and one players doesnt work yet")
    players = eval(input("1 or 2 players?: "))
    if (players) != 2: print("This functionality isn't there yet")
    newgame = input("Write n for newgame or c for continue: Doesnt work yet always starts a new game just enter n")
    first = "X"
    second = "O"
    print(game[0])
    print(game[1])
    print(game[2])
    won = False
    while won == False:
        legalmove = False
        while legalmove == False:
            firstx = int(input("First Player enter row: "))
            firsty = int(input("First Player enter column: "))
            if (game[firstx - 1][firsty - 1] == "-"):
                game[firstx - 1][firsty - 1] = first
                legalmove = True
            else:
                print("Not a legal move")
        print(game[0])
        print(game[1])
        print(game[2])
        if (checkgame(game)) == True:
            print("First player wins")
            won = True
            break
        legalmove = False
        while legalmove == False:
            secondx = int(input("Second Player enter row between 1 and 3: "))
            secondy = int(input("Second Player enter column between 1 and 3: "))
            if (game[secondx - 1][secondy - 1] == "-"):
                game[secondx - 1][secondy - 1] = second
                legalmove = True
            else:
                print("Not a legale move")
        print(game[0])
        print(game[1])
        print(game[2])
        if (checkgame(game)) == True:
            print("Second player wins")
            won = True
            break
    
def checkgame(game):
    if (game[0][0] != "-") and (game[0][0] == game[0][1]) and (game[0][1] == game[0][2]): return True
    elif (game[1][0] != "-") and (game[1][0] == game[1][1]) and (game[1][1] == game[1][2]): return True
    elif (game[2][0] != "-") and (game[2][0] == game[2][1]) and (game[2][1] == game[2][2]): return True
    elif (game[0][0] != "-") and (game[0][0] == game[1][0]) and (game[1][0] == game[2][0]): return True
    elif (game[0][1] != "-") and (game[0][1] == game[1][1]) and (game[1][1] == game[2][1]): return True
    elif (game[0][2] != "-") and (game[0][2] == game[1][2]) and (game[1][2] == game[2][2]): return True
    elif (game[0][0] != "-") and (game[0][0] == game[1][1]) and (game[1][1] == game[2][2]): return True
    elif (game[2][0] != "-") and (game[2][0] == game[1][1]) and (game[1][1] == game[0][2]): return True
    elif (game[0][0] != "-") and (game[0][1] != "-") and (game[0][2] != "-") and (game[1][0] != "-") and (game[1][1] != "-") and (game[1][2] != "-") and (game[2][0] != "-") and (game[2][1] != "-") and (game[2][2] != "-"): return True
    else: return False
main()

