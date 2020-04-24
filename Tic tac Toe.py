#This function will display the board
def display_board(board):
    i=0
    while i < len(board):
         print ('{} | {} | {}'.format(board[i],board[i+1],board[i+2]))
         print('---------')
         i = i +3


#This function will take input from user regarding the mark
def player_input():
    marker=''
    while marker !='X' and marker !='x'   and marker != 'O' and marker !='o' :
         marker=input('Player 1.....Please select "X" or "O" : ')
    if marker =='X'or marker =='x':
        return('X','O')
    else:
         return('O','X')


#This section will place the marker in the board based on the user's input
def place_marker(board, marker, position):
    i=0
    pos=int(position)
    pp=pos-1
    while i<len(board):
        board[pp]=marker
        i=i+1


#This section will check if a player won the match
def win_check(board, mark):
    return ((board[6] ==  board[7] ==  board[8] == mark) or # across the top
    (board[3] ==  board[4] ==  board[5] == mark) or # across the middle
    (board[0] ==  board[1] ==  board[2] == mark) or # across the bottom
    (board[6] ==  board[3] ==  board[0] == mark) or # down the middle
    (board[7] ==  board[4] ==  board[1] == mark) or # down the middle
    (board[8] ==  board[5] ==  board[2] == mark) or # down the right side
    (board[6] ==  board[4] ==  board[2] == mark) or # diagonal
    (board[8] ==  board[4] ==  board[0] == mark)) # diagonal



#This section will choose which player will go first
import random
def choose_first():
    random_player=random.randint(1, 2)
    return random_player

#This section will check if a position is empty or not
def space_check(board, position):
    marks=['X','x','O','o']
    pos=int(position)
    if board[pos] in marks:
        return print('this poisition is occupied')
    else:
        return print('This position is free')

#This section will check if the board is full or not
def full_board_check(board):

    marks=['X','x','O','o']
    creck=all(elem in marks for elem in board)
    if creck:
        return True

#This section will take the input from user
def player_choice(board):
    position=input('Enter the next position = ')
    #space_check(board, position)
    return position




#From here the actual code is started
print('Welcome to Tic Tac Toe')
theBoard = [1,2,3,4,5,6,7,8,9]
display_board(theBoard)
print('\n')

#player_input()
player1_mark,player2_mark=player_input()
print("Player 1's mark is this = {} and Player 2's mark is this = {}".format(player1_mark,player2_mark))
print('\n \n')

player=choose_first()
player_SecondPart= player
print('Player {} will go first'.format(player))
counter = 0
game_on=True

#while game_on==True:
i=0
while i<5:
    if player==1:

        pos=player_choice(theBoard)
        place_marker(theBoard, player1_mark, pos)
        player=2

    else:

        pos=player_choice(theBoard)
        place_marker(theBoard, player2_mark, pos)
        player=1
    newBoard=theBoard
    display_board(newBoard)
    i=i+1


if win_check(newBoard, player1_mark)==True:
    print('Player 1 Won')
elif win_check(newBoard, player2_mark)==True:
    print('Player 2 Won')
elif win_check(newBoard, player2_mark)==False:
    j=0
    win=''
    while j<5:
        if player_SecondPart==1:
            pos=player_choice(newBoard)
            place_marker(theBoard,player2_mark,pos)
            if win_check(newBoard, player2_mark)==True:
                display_board(newBoard)
                win='Player 2 win'
                print(win)
                break
            else:
                if full_board_check(newBoard)==True:
                    display_board(newBoard)
                    print("It's a draw")
                    break
                else:
                    display_board(newBoard)
                    player_SecondPart=2

        elif player_SecondPart==2:
            pos=player_choice(newBoard)
            place_marker(newBoard,player1_mark,pos)
            if win_check(newBoard, player1_mark)==True:
                display_board(newBoard)
                win='Player 1 win'
                print(win)
                break
            else:
                if  full_board_check(newBoard)==True:
                    display_board(newBoard)
                    print("It's a draw")
                    break
                else:
                    display_board(newBoard)
                    player_SecondPart=1

    j=j+1



