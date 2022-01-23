def create_board():
    board_size = input("for playing on 3X3 board press 0\n"
                       "for playing on 4X4 board press 1\n")
    if board_size == "0":
        table3 = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        return table3
    elif board_size == "1":
        table4 = [["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_"]]
        return table4
    else:
        print("invalid input")
        return create_board()


def print_board(board):
    for row in board:
        print(row)


def example_board():
    t3row1 = ["1", " _ ", " _ ", " _ "]
    t3row2 = ["2", " _ ", " _ ", " _ "]
    t3row3 = ["3", " _ ", " X ", " _ "]
    t3row4 = ["*", " 1 ", " 2 ", " 3 "]
    print(f"{t3row1}\n{t3row2}\n{t3row3}\n{t3row4}")
    t4row1 = ["1", " _ ", " _ ", " _ ", " _ "]
    t4row2 = ["2", " _ ", " _ ", " _ ", " _ "]
    t4row3 = ["3", " _ ", " X ", " _ ", " _ "]
    t4row4 = ["4", " _ ", " _ ", " _ ", " _ "]
    t4row5 = ["*", " 1 ", " 2 ", " 3 ", " 4 "]
    print(f"{t4row1}\n{t4row2}\n{t4row3}\n{t4row4}\n{t4row5}")


def choose_mode():
    game_mode = input("for playing with a friend press 0\n")
    if game_mode == "0":
        return 0
    else:
        print("invalid input")
        return choose_mode()


def choose_symbol():
    symbol = input("player 1 please choose your symbol\nfor 'X' press X\nfor 'O' press O\n").upper()
    if symbol == "X":
        return True
    elif symbol == "O":
        return False
    else:
        print("invalid input")
        return choose_symbol()


def game_still_running(board):
    for row in board:
        for ta in row:
            if ta == '_':
                return False

    return True


def check_position(board):
    pos = input("please type your chosen position\nfirst choose the column and then the row\n")
    if pos.isdigit():
        pos = int(pos)
        if 11 <= pos <= 44:
            row = pos % 10 - 1
            column = pos // 10 - 1
            if 0 <= row <= 3 and 0 <= column <= 3 and len(board) == 4:
                return pos
            elif 0 <= row <= 2 and 0 <= column <= 2 and len(board) == 3:
                return pos
            else:
                print("invalid input")
                return check_position(board)
        else:
            print("invalid input")
            return check_position(board)

    else:
        print("invalid input")
        return check_position(board)


def check_win(board):
    for symbol in ['X', 'O']:
        if len(board) == 3:
            if board[0].count(symbol) == 3 or board[1].count(symbol) == 3 or board[2].count(symbol) == 3:
                return symbol
            elif board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol:
                return symbol
            elif board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol:
                return symbol
            elif board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol:
                return symbol
            elif board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
                return symbol
            elif board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
                return symbol
            else:
                return 'NoWin'
        if len(board) == 4:
            if board[0].count(symbol) == 4 or board[1].count(symbol) == 4 or board[2].count(symbol) == 4 or \
                    board[3].count(symbol) == 4:
                return symbol
            elif board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol and board[3][0] == symbol:
                return symbol
            elif board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol and board[3][1] == symbol:
                return symbol
            elif board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol and board[3][2] == symbol:
                return symbol
            elif board[0][3] == symbol and board[1][3] == symbol and board[2][3] == symbol and board[3][3] == symbol:
                return symbol
            elif board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol and board[3][3] == symbol:
                return symbol
            elif board[0][3] == symbol and board[1][2] == symbol and board[2][1] == symbol and board[3][0] == symbol:
                return symbol
            else:
                return "NoWin"


# ----------------------------------------------------------------------------------------------------------------------
print("Welcome to TicTacToe game")
helpGame = input("press 'h' to get help\npress any key to continue\n").lower()
if helpGame == "h":
    print("you will have to type the column first and then the row\nfor example '23':")
    example_board()

game_board = create_board()
mode = choose_mode()
gameRunning = True
p1symbol = choose_symbol()
print("please type your chosen position\nfirst choose the column and then the row\n")
print_board(game_board)
turn = p1symbol
while gameRunning:
    if mode == 0:
        position = check_position(game_board)
        r = position % 10 - 1
        c = position // 10 - 1
        if turn:
            game_board[r][c] = "X"

        else:
            game_board[r][c] = "O"

        if check_win(game_board) == 'X' and turn:
            print('The winner is the X player.')
            gameRunning = False
        elif check_win(game_board) == 'O' and not turn:
            print('The winner is the O player.')
            gameRunning = False
        elif game_still_running(game_board):
            print("It's a draw.")
            gameRunning = False

        if turn:
            turn = False
        else:
            turn = True
        print_board(game_board)
