def find_location(board):
    x = 0
    y = 0
    for i in range(len(board)):
        for ii in range(len(board)):
            if board[i][ii] == 1:
                x = ii
                y = i

    return x, y



def posible_moves(x, y, board_size):
    posible_moves_array = []

    if y > 0:
        posible_moves_array.append("(N)orth")

    if x < (board_size-1):
        posible_moves_array.append("(E)ast")
    if y < (board_size-1):
        posible_moves_array.append("(S)outh")
    if x > 0:
        posible_moves_array.append("(W)est")



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
    choose_move = ""
    keepgoing = True
    while keepgoing:
        print("You can travel:", end = " ")
        for i in range(len(posible_moves_arry)):
            if (i + 1) == len(posible_moves_array):
                print(posible_moves_arry[i], end=".")
            else:
                print(posible_moves_arry[i], end=" or ")
                

        print("")
        choose_move = str(input("Direction: "))


        for i in range(len(posible_moves_arry)):
            if choose_move == "n" or choose_move == "N":
                if posible_moves_arry[i] == "(N)orth":
                    keepgoing = False
                    break

            if choose_move == "s" or choose_move == "S":
                if posible_moves_arry[i] == "(S)outh":
                    keepgoing = False
                    break

            if choose_move == "e" or choose_move == "E":
                if posible_moves_arry[i] == "(E)ast":
                    keepgoing = False
                    break

            if choose_move == "w" or choose_move == "W":
                if posible_moves_arry[i] == "(W)est":
                    keepgoing = False
                    break

        if keepgoing:
            print("Not a valid direction!")

    change_y = 0
    change_x = 0
    if choose_move == "n" or choose_move == "N":
        change_y = -1
    if choose_move == "s" or choose_move == "S":
        change_y = 1
    if choose_move == "e" or choose_move == "E":
        change_x = 1
    if choose_move == "w" or choose_move == "W":
        change_x = -1

    board[y][x] = 0
    board[(y + change_y)][(x + change_x)] = 1

    return board


board_size = 3
board = [[0 for x in range(board_size)] for y in range(board_size)]
board[2][0] = 1

not_winner = True

while not_winner:
    x_loc, y_loc = find_location(board)

    posible_moves_array = posible_moves(x_loc, y_loc, board_size)
    board = move_player(posible_moves_array, x_loc, y_loc, board)

    x_loc, y_loc = find_location(board)
    if x_loc == 2 and y_loc == 2:
        print("Victory!")
        not_winner = False




