# Tic-Tac-Toe Game

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i] + "|" + board[i + 1] + "|" + board[i + 2])
        if i < 6:
            print("-+-+-")

# Function to check for a win
def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check for a draw
def check_draw(board):
    return " " not in board

# Function to get valid player move
def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number (1-9).")

# AI opponent's move using a simple rule-based strategy
def get_ai_move(board):
    for i in range(9):
        if board[i] == " ":
            return i

# Main game loop
player_turn = True
while True:
    print_board(board)
    
    if player_turn:
        move = get_player_move(board)
        board[move] = "X"
    else:
        move = get_ai_move(board)
        board[move] = "O"

    if check_win(board, "X"):
        print_board(board)
        print("You win!")
        break
    elif check_win(board, "O"):
        print_board(board)
        print("AI wins!")
        break
    elif check_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    player_turn = not player_turn
