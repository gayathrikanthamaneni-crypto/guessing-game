# Simple Tic Tac Toe game in Python

# Draw the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check for a win
def check_win(board, player):
    # Rows, columns, diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

# Main game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        # Check if move is valid
        if board[row][col] != " ":
            print("Spot taken! Try again.\n")
            continue

        # Make move
        board[row][col] = current_player

        # Check win
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        # Check tie
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("🤝 It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
