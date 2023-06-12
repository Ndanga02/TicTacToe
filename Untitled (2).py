#!/usr/bin/env python
# coding: utf-8

# In[6]:


game_board = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]

def printBoard(game_board):
    
    clear_output()
    print('CURRENT BOARD:\n')
    print(' -----------')
    print('| ' + game_board[0][0] + ' | ' + game_board[0][1] + ' | ' + game_board[0][2] + ' |')
    print(' -----------')

    print('| ' + game_board[1][0] + ' | ' + game_board[1][1] + ' | ' + game_board[1][2] + ' |')
    print(' -----------')

    print('| ' + game_board[2][0] + ' | ' + game_board[2][1] + ' | ' + game_board[2][2] + ' |')
    print(' -----------')


# In[2]:


def play_on():
    choice = ''
    while choice not in ['Y', 'N']:
        choice = input('Would you like to keep on playing? Y or N --> ')
        if choice not in ['Y', 'N']:
            print('I do not understand, select Y or N ')
    if choice == 'Y':
        return True
    else:
        return False


# In[3]:


from IPython.display import clear_output

def player1_and_2(game_board, player_1, player_2):
    position1 = ''
    print('Player 1, your turn')
    while position1 not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        position1 = input('Enter a move between 0 and 8 --> ')
        if position1.isdigit() and int(position1) in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            position1 = int(position1)
        else:
            print('Please enter a valid move')

    if position1 in [0, 1, 2]:
        game_board[0][position1] = player_1

    elif position1 in [3, 4, 5]:
        if position1 == 3:
            position1 = 0
        elif position1 == 4:
            position1 = 1
        elif position1 == 5:
            position1 = 2
        game_board[1][position1] = player_1

    elif position1 in [6, 7, 8]:
        if position1 == 6:
            position1 = 0
        elif position1 == 7:
            position1 = 1
        elif position1 == 8:
            position1 = 2
        game_board[2][position1] = player_1

    printBoard(game_board)
    if win(game_board, player_1):
        return False

    position2 = ''

    print('Player 2, your turn')
    while position2 not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        position2 = input('Enter a move between 0 and 8 --> ')
        if position2.isdigit() and int(position2) in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            position2 = int(position2)
        else:
            print('Please enter a valid move')

    clear_output()

    if position2 in [0, 1, 2]:
        game_board[0][position2] = player_2

    elif position2 in [3, 4, 5]:
        if position2 == 3:
            position2 = 0
        elif position2 == 4:
            position2 = 1
        elif position2 == 5:
            position2 = 2
        game_board[1][position2] = player_2

    elif position2 in [6, 7, 8]:
        if position2 == 6:
            position2 = 0
        elif position2 == 7:
            position2 = 1
        elif position2 == 8:
            position2 = 2
        game_board[2][position2] = player_2

    printBoard(game_board)
    if win(game_board, player_2):
        return False

    return True


# In[4]:


import random

def win(game_board, player):
    random_message = ['Fine move!', 'Lets gooo', 'Hmm Ok I guess', 'Damn', 'Awesome', 'You Rock', 'Stop it I love it',
                      'Where are your manners?']

    if game_board[0][2] == game_board[1][1] == game_board[2][0] == player:
        print('Congratulations! ' + player + ' won!')
        return True
    elif game_board[0][0] == game_board[1][1] == game_board[2][2] == player:
        print('Congratulations! ' + player + ' won!')
        return True
    elif game_board[0][1] == game_board[1][1] == game_board[2][1] == player:
        print('Congratulations! ' + player + ' won!')
        return True

    elif game_board[1][0] == game_board[1][1] == game_board[1][2] == player:
        print('Congratulations! ' + player + ' won!')
        return True
    elif game_board[0][0] == game_board[1][0] == game_board[2][0] == player:
        print('Congratulations! ' + player + ' won!')
        return True
    elif game_board[0][0] == game_board[0][1] == game_board[0][2] == player:
        print('Congratulations! ' + player + ' won!')
        return True
    elif game_board[2][0] == game_board[2][1] == game_board[2][2] == player:
        print('Congratulations! ' + player + ' won!')
        return True
    elif game_board[0][2] == game_board[1][2] == game_board[2][2] == player:
        print('Congratulations! ' + player + ' won!')
        return True
    else:
        print(random.choice(random_message))
        return False


# In[7]:


game_on = True

while game_on:
    print('WELCOME TO TIC TAC TOE:\n')
    printBoard(game_board)
    player_1 = ''
    player_2 = ''

    while player_1 not in ['X', 'O']:
        player_1 = input('Player 1, Select X or O --> ')
        if player_1 not in ['X', 'O']:
            print('Please select the correct symbol')

    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'

    game_board = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
    win_or_continue = True

    while win_or_continue:
        win_or_continue = player1_and_2(game_board, player_1, player_2)

    game_on = play_on()


# In[ ]:




