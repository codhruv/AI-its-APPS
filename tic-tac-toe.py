import math

# Initialize board
board = [" " for _ in range(9)]

# Function to print board
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Function to check winner
def check_winner(b, player):
    # All possible win conditions
    win_cond = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for cond in win_cond:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] == player:
            return True
    return False

# Function to check if board is full
def is_full(b):
    return " " not in b

# Minimax function
def minimax(b, depth, is_maximizing):
    if check_winner(b, "O"):   # AI wins
        return 1
    if check_winner(b, "X"):   # Human wins
        return -1
    if is_full(b):             # Draw
        return 0

    if is_maximizing:  # AI's turn
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:  # Human's turn
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

# Function to get best move for AI
def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue
        board[move] = "X"

        print_board()
        if check_winner(board, "X"):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = "O"
        print("\nAI plays:")
        print_board()

        if check_winner(board, "O"):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break


# Run the game
play_game()
