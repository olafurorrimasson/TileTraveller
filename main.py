board_size = 3
board = [[0 for x in range(board_size)] for y in range(board_size)]


board[0][2] = 1


while 

def find_location(board):
    x = 0
    y = 0
    for i in range(len(board)):
        for ii in range(len(board)):
            if board[i][ii] == 1:
                x = i
                y = ii

    return x, y



def posible_moves(x, y, board_size):
    posible_moves_array = []
    if x < (board_size-1):
        posible_moves_array.append("(E)ast")
    if x > 0:
        posible_moves_array.append("(W)est")
    if y < (board_size-1):
        posible_moves_array.append("(S)outh")
    if y > 0:
        posible_moves_array.append("(N)orth")

    #removing where there are walls
    if x == 1 and y == 0:
        posible_moves_array.remove("(S)outh")
    if x == 2 and y == 1:
        posible_moves_array.remove("(W)est")
    if x == 1 and y == 1:
        posible_moves_array.remove("(N)orth")
        posible_moves_array.remove("(E)ast")
    if x == 0 and y == 2:
        posible_moves_array.remove("(E)ast")
    if x == 1 and y == 2:
        posible_moves_array.remove("(W)est")
        posible_moves_array.remove("(E)ast")
    if x == 2 and y == 2:
        posible_moves_array.remove("(W)est")

    return posible_moves_array

def move_player(posible_moves_arry, x, y, board):
    while True:
        print("You can travel:", end = " ")
        for i in range(len(posible_moves_arry)):
            print(posible_moves_arry, end=" ")

        choose_move = str(input("Direction:"))

        for i in range(len(posible_moves_arry)):
            if choose_move == "n" or choose_move == "N":
                if posible_moves_arry[i] == "(N)orth":
                    break
            if choose_move == "s" or choose_move == "S":
                if posible_moves_arry[i] == "(S)outh":
                    break
            if choose_move == "e" or choose_move == "E":
                if posible_moves_arry[i] == "(E)ast":
                    break
            if choose_move == "w" or choose_move == "W":
                if posible_moves_arry[i] == "(W)est":
                    break






