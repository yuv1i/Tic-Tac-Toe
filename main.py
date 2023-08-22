import random

# Initialize the game board
board = [' ' for _ in range(9)]
currentPlayer = "X"
winner = None
gameRunning = True

# Function to print the game board with colorful formatting
def printBoard(board):
    print("\nLet's play Tic-Tac-Toe!\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")
        if i < 6:
            print("---+---+---")

# Function to take player input
def playerInput(board):
    while True:
        print(f"\nPlayer ({currentPlayer}), it's your turn.")
        try:
            inp = int(input("Enter a number 1-9 to place your mark: "))
            if inp >= 1 and inp <= 9 and board[inp - 1] == ' ':
                board[inp - 1] = currentPlayer
                break
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

# Function to check for a win
def checkWin():
    global winner
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            winner = currentPlayer
            return True

# Function to check for a tie
def checkTie(board):
    global gameRunning
    if ' ' not in board:
        printBoard(board)
        print("\nIt's a tie! Game Over.")
        gameRunning = False

# Function to switch the current player
def switchPlayer():
    global currentPlayer
    currentPlayer = "X" if currentPlayer == "O" else "O"

# Main game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    if checkWin():
        printBoard(board)
        print(f"\nCongratulations, Player ({winner})! You won!")
        break
    checkTie(board)
    switchPlayer()
