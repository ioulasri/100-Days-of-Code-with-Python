import random

board = [[' ',' ',' '], [' ',' ',' '],[' ',' ',' ']]
player = 'X'
AI = '0'
def print_table():
    for row in board:
        print(' | '.join(row))
        print('---------')


def user_input():
    global player, AI
    X_O = input("choose between 'O' or 'X'")
    if X_O == 'X':
        player = 'X'
        AI = 'O'
    else:
        player = 'O'
        AI = 'X'
print_table()

def player_playing():
    while True:
        position = input("choose a position in the board: ")
        while True:
            if int(position[0]) <= 2 and int(position[1]) <= 2:
                break
            position = input("choose a position in the board: ")
        if board[int(position[0])][int(position[1])] == ' ':
            board[int(position[0])][int(position[1])] = player
            break

def ai_playing():
    while True:
        a = random.randint(0, 2)
        b = random.randint(0, 2)
        if board[a][b] == ' ':
            break
    board[a][b] = AI

def win(current_player):
    for i in range(0, 3):
        win = 0
        for j in range(0, 3):
            if board[i][j] == current_player:
                win += 1
                if win == 3:
                    return 1
    for i in range(0, 3):
        win = 0
        for j in range(0, 3):
            if board[j][i] == current_player:
                win += 1
                if win == 3:
                    return 1
    for i in range(0, 3):
        win = 0
        if board[i][i] == current_player:
            win += 1
            if win == 3:
                return 1
    if  board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player:
        return 1
    if  board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player:
        return 1
def draw_game():
    draw = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == player or board[i][j] == AI:
                draw += 1
                if draw == 9:
                    return 1

def check_player_won():
    pass
def game():
    user_input()
    winner_p = 0
    winner_a = 0
    draw = 0
    while True:
        draw = draw_game()
        if draw == 1:
            print_table()
            print('Ta3adol')
            quit()
        player_playing()
        draw = draw_game()
        if draw == 1:
            print_table()
            print('Ta3adol')
            quit()
        winner_p = win(player)
        if winner_p == 1:
            print_table()
            print("nadi")
            quit()
        ai_playing()
        draw = draw_game()
        if draw == 1:
            print_table()
            print('Ta3adol')
            quit()
        winner_a = win(AI)
        if winner_a == 1:
            print_table()
            print("demdoma")
            quit()
        print_table()
        winner = win(AI)





game()