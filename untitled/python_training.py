# ---- Global Variables ----
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

game_still_going = True
# If game is still going

winner = None
# Who won? Or Tie

current_player = "X"

# ---- End of global variables ----


def display_board():
# The dislpay of the board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game ():
# The play of the game
    display_board()
    # displays initial board

    while game_still_going:

        handle_turn(current_player)
        # handle a single turn of a player

        check_if_game_over()
        # Check if game is over

        flip_player()
        # Flip to other player

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie...")
# The game has ended



def handle_turn(player):

    print(player + "'s turn.")
    position = input(" Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input(" Choose another position from 1-9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can not do that!")
    board[position] = player
    display_board()

def check_if_game_over():

    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    # writing to global variable win. Need to refer to it in the code
    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        #there was no win
        winner = None
    return

def check_rows():
    global game_still_going
    # Need to pull from global variables
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # This checks to see if the rows all have the same character and not empty
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    # This is to return the winner

    return



def check_columns():
    global game_still_going
    # Need to pull from global variables
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # This checks to see if the columns all have the same character and not empty
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # This is to return the winner
    return

def check_diagonals():
    global game_still_going
    # Need to pull from global variables
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # This checks to see if the diagonals all have the same character and not empty
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1 or diagonal_2:
        return board[4]
    # This is to return the winner
    return



def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
        # if current player was X, switch to O
    elif current_player == "O":
        current_player = "X"
        # else if current player id O, switch to X
    return


play_game()





