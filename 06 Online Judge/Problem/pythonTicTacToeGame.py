# Tic Tac Toe (2 Player)
# Author: Faruk Example

def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_winner(board, player):
    # All winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def tic_tac_toe():
    board = [" " for _ in range(9)]
    current_player = "X"
    move_count = 0

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        move = input("Choose a position (1-9): ")

        # Input check
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input! Please enter a number 1-9.")
            continue

        move = int(move) - 1
        if board[move] != " ":
            print("That spot is already taken!")
            continue

        # Move set
        board[move] = current_player
        move_count += 1

        # Check winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Draw check
        if move_count == 9:
            print_board(board)
            print("It's a draw!")
            break

        # Player switch
        current_player = "O" if current_player == "X" else "X"

# Program start
if __name__ == "__main__":
    tic_tac_toe()
