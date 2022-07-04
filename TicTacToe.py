import random


# create coloumn for row
board = [" "] * 9

# Function to make a row 3 coloumn per row (you can build your own!) ===BELOW THIS===


def draw_board(board):
    # This is creating 1st row with 3 coloum
    row_1 = "{}|{}|{}".format(board[0], board[1], board[2])
    # This is creating 2nd row with 3 coloum
    row_2 = "{}|{}|{}".format(board[3], board[4], board[5])
    # This is creating 3rd row with 3 coloum
    row_3 = "{}|{}|{}".format(board[6], board[7], board[8])
    # Show the result
    print(row_1+'\n'+row_2+'\n'+row_3+'\n')


# Function to let user move/choice where user want to put X or O ===BELOW THIS===


def user_move(board, user_type):
    # Let user input 1-9, its minus one because List(array) start from 0, so it should be -1 or it will be out of range
    user_choice = int(input('Choose between 1-9 : ')) - 1

    # Below is the condition, If user choice numbers that have been choosed before, it will tell its already taken and let user try again
    if board[user_choice] != ' ':
        print('Space already taken!. Try again!')
        # This call the function again, because user gonna input again
        user_move(board, user_type)
    else:
        # it will place the numbers that user input to the board
        board[user_choice] = user_type
        available_spaces.remove(user_choice)


def comp_move(board, user_type):
    computer_choice = random.choice(available_spaces)
    board[computer_choice] = user_type
    available_spaces.remove(computer_choice)


# Check if there any 3 same letter wether its X or O in 3 Straight line, Vertical or Horizontal ===BELOW THIS===


def check_win(board, x_o):
    # Im sorry its gonna be LONG LONG LONG WAY CODE. but the main thing is , it will generate all the possibility move to win, 3 Horizontal or 3 vertical and the same letter X or O
    if board[0] == x_o and board[1] == x_o and board[2] == x_o or board[3] == x_o and board[4] == x_o and board[5] == x_o or board[6] == x_o and board[7] == x_o and board[8] == x_o or board[0] == x_o and board[3] == x_o and board[6] == x_o or board[1] == x_o and board[4] == x_o and board[7] == x_o or board[2] == x_o and board[5] == x_o and board[8] == x_o or board[0] == x_o and board[4] == x_o and board[8] == x_o or board[2] == x_o and board[4] == x_o and board[6] == x_o:
        play = False  # If there is condition above, it will end the game change the 'play' variable to False and not Looping on the while
        print('Yeay!! {} has won the game!!.'.format(x_o))
    else:
        play = True  # Will play again
    return play


# Create some Variable, play as play to strat the game or stop, board we call the coloumn again, draw board we call the fixed board for the game (3 col , 3 row)
play = True  # Variable to start the loop
board = [" "] * 9  # call the coloumn again
available_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
draw_board(board)  # The result or the fixed board for playing
comp_or_friend = input(
    "Would you like to play againts Computer or Friends ? ('c or f') : ")


# The game started
while play == True:

    # This is function that user X is move wherever the coloumn that he choose
    user_move(board, 'x')
    # this let the play check is there any condition to win
    play = check_win(board, 'x')
    if play == False:  # If there isnt any win condition, it will continue to play again
        continue
    draw_board(board)  # It will store the user input to the board

    if comp_or_friend == 'f':
        # This is user O function to move wherever the coloumn that he choose
        user_move(board, 'o')
    elif comp_or_friend == 'c':
        comp_move(board, 'o')

    # this let the play check is there any condition to win
    play = check_win(board, 'o')
    draw_board(board)  # It will store the user input to the board


print('End of the game!')  # If the games End, it will Appear :)
