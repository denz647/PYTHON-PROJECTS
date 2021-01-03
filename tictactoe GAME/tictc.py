board=["-","-","-",
       "-","-","-",
       "-","-","-"]

winner=None
game_is_working=True
current_player="X"
def play_game():
    display_board()
    while game_is_working:
        handle_turn(current_player)
        check_gameover()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner+" WON!!")
    elif winner==None:
        print("tie!!")

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def handle_turn(player):
    print(player+"'s turn")
    position=input("enter position from 1-9:  ")
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = player

    # Show the game board
    display_board()


def check_gameover():
    check_winner()
    check_tie()
def check_winner():
    global winner
    row_winner=check_row()
    column_winner=check_column()
    diagonal_winner=check_diagonal()
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
def check_row():
    global game_is_working
    row1=board[0]==board[1]==board[2]!="-"
    row2=board[3]==board[3]==board[4]!="-"
    row3=board[6]==board[7]==board[8]!="-"
    if row1 or row2 or row3:
        game_is_working=False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None
def check_column():
    global game_is_working
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        game_is_working=False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    else:
        return None
def check_diagonal():
    global game_is_working
    diag1=board[0]==board[4]==board[8]!="-"
    diag2=board[2]==board[4]==board[6]!="-"
    if diag1 or diag2:
        game_is_working=False
    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    else:
        return None

def check_tie():
    global game_is_working
    if "-" not in board:
        game_is_working=False
        return True
    else:
        return False

def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"


play_game()
