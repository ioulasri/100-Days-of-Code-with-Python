from typing import List, Tuple

# The values of the cells on the board:
# X: 1
# O: -1
# Empty: 0

# The AI is X and the opponent is O

# A simple representation of the tic-tac-toe board as a 2D array
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def get_possible_moves(board: List[List[int]]) -> List[Tuple[int, int]]:
    # Return a list of all empty cells on the board
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                moves.append((i, j))
    return moves


def evaluate(board: List[List[int]]) -> int:
    # Count the number of lines of three that the AI has and
    # subtract the number of lines that the opponent has
    score = 0
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2]:
            score += board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i]:
            score += board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        score += board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        score += board[0][2]
    return score


def minimax(board: List[List[int]], player: int) -> Tuple[int, Tuple[int, int]]:
    # Base case: the game is over and we return the score
    if game_over(board):
        return evaluate(board), (-1, -1)

    # Initialize the best score and the best move
    best_score = -2 * player
    best_move = (-1, -1)

    # Consider all possible moves
    for move in get_possible_moves(board):
        # Make the move
        board[move[0]][move[1]] = player
        # Recursively find the best move for the other player
        score, _ = minimax(board, -player)
        # Undo the move
        board[move[0]][move[1]] = 0
        # Update the best score and move if necessary
        if player == 1:
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move
    return best_score, best_move


def play_game():
    while not game_over(board):
        # The AI makes the first move
        score, move = minimax(board, 1)
        board[move[0]][move[1]] = 1
        if game_over(board):
            print_board(board)
            break
        # The opponent makes a move
        move = get_opponent_move()
        board[move[0]][move[1]] = -1
        print("Opponent moves to", move)
        print_board(board)
    # The game is over, determine the result
    if evaluate(board) == 1:
        print("AI wins!")
    elif evaluate(board) == -1:
        print("Opponent wins!")
    else:
        print("It's a draw!")


def print_board(board: List[List[int]]):
    # Print the board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                print("X", end=" ")
            elif board[i][j] == -1:
                print("O", end=" ")
            else:
                print(" ", end=" ")
            if j < 2:
                print("|", end=" ")
        print()
        if i < 2:
            print("---------")
    print()


def game_over(board: List[List[int]]) -> bool:
    # Return True if the game is over, False otherwise
    # The game is over if one player has won or the board is full
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


def get_opponent_move() -> Tuple[int, int]:
    # Prompt the user for their next move
    while True:
        move = input("Enter your move (row column): ")
        try:
            i, j = map(int, move.split())
            if i in [0, 1, 2] and j in [0, 1, 2] and board[i][j] == 0:
                return i, j
            print("Invalid move, try again")
        except ValueError:
            print("Invalid input, try again")


play_game()
