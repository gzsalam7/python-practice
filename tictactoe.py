board = [["S", "S", "S"],["S", "S", "S"],["S", "S", "S"]]

def main():
    print("Welcome to the tictactoe app: ")
    x = input("Num of players????: ")
    if int(x) != 2:
        print("sry")
        return 0
    print("welcome!")
    n = input("new game or continue? 1 or 2")
    if n == 2:
        y = input("Enter initial state: ")
        nb = []
        for i in y:
            if (i == "X") or (i == "O"):
                nb.append(i)
            else:
                nb.append("S")
        B = nb[:3]
        C = nb[3:6]
        D = nb[6:10]
        nb2 = []
        nb2.append(B)
        nb2.append(C)
        nb2.append(D)
    else:
        nb2 = board
    print(nb2)
    if win(nb2) == True:
        print("someone already won")
        return 0
    p1 = input("Player 1 character?: ")
    p2 = input("Player 2 character?: ")
    w = False
    while w == False:
        gg = False
        while gg == False:
            p1x = input("player 1: x coordinate (row): ")
            p1y = input("player 1: y (column): ")
            p1x= int(p1x)
            p1y = int(p1y)
            if (nb2[p1x - 1][p1y - 1] == "S"):
                nb2[p1x - 1][p1y - 1] = p1
                gg = True
            else:
                print("There's already something there! Try again")
        for z in nb2:
            print(z)
        if (win(nb2) == True):
            print("Player 1 wins")
            w = True
            return 1
            

        
        gg = False
        while gg == False:
            p2x = input("player 2: x coordinate (row): ")
            p2y = input("player 2: y (column): ")
            p2x= int(p2x)
            p2y = int(p2y)
            if (nb2[p2x - 1][p2y - 1] == "S"):
                nb2[p2x - 1][p2y - 1] = p2
                gg = True
            else:
                print("There's already something there! Try again")
        for z in nb2:
            print(z)
        if (win(nb2) == True):
            print("Player 2 WINS")
            w = True
            return 2

def win(board):
    if (board[0][0] != "S") and (board[0][0] == board[0][1]) and (board[0][1] == board[0][2]):
        return True
    elif (board[1][0] != "S") and (board[1][0] == board[1][1]) and (board[1][1] == board[1][2]):
        return True
    elif (board[2][0] != "S") and (board[2][0] == board[2][1]) and (board[2][1] == board[2][2]):
        return True
    elif (board[0][0] != "S") and (board[0][0] == board[1][0]) and (board[1][0] == board[2][0]):
        return True
    elif (board[0][1] != "S") and (board[0][1] == board[1][1]) and (board[1][1] == board[2][1]):
        return True
    elif (board[0][2] != "S") and (board[0][2] == board[1][2]) and (board[1][2] == board[2][2]):
        return True
    elif (board[0][0] != "S") and (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
        return True
    elif (board[2][0] != "S") and (board[2][0] == board[1][1]) and (board[1][1] == board[0][2]):
        return True
    else:
        return False
main()
