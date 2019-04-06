from graphics import *
import sys
from time import sleep

# input and assign each player's name and color
Player_1 = input('Player 1 print your name: ')
color_1 = input('Player 1 pick a color: ')
Player_2 = input('Player 2 Print your name: ')
color_2 = input('Player 2 pick a color: ')

# input the board size, must be an integer and larger than 2
N = int(input('Please enter the board size: '))
if N < 3:
    sys.exit('Error: please enter a valid integer larger than 2')

# define the board length in relation to N in pixels
length = (N * 100 + 200)
win = GraphWin("Tic Tac Toe", length, length)

# define where the win/tie statement will be shown and the color that will be displayed
win1 = Text(Point((length/2), (length-50)), ('{} wins!'.format(Player_1)))
win1.setSize(36)
win1.setTextColor(color_1)
win2 = Text(Point((length/2), (length-50)), ('{} wins!'.format(Player_2)))
win2.setSize(36)
win2.setTextColor(color_2)
tie = Text(Point((length/2), (length-50)), "Tie Game!")
tie.setSize(36)
tie.setTextColor(color_rgb(255, 0, 0))

# function that creates the board
def board():

    # writes the player 1/2 and the name of the player on the board
    play1 = Text(Point(100, 20), 'Player 1: ')
    play1.setSize(18)
    play1.draw(win)
    name1 = Text(Point(100, 50), Player_1)
    name1.setSize(22)
    name1.setTextColor(color_1)
    name1.draw(win)

    play2 = Text(Point(((N+1) * 100), 20), 'Player 2: ')
    play2.setSize(18)
    play2.draw(win)
    name2 = Text(Point(((N+1) * 100), 50), Player_2)
    name2.setSize(22)
    name2.setTextColor(color_2)
    name2.draw(win)

    # draws the lines of the board in relation to N and length
    while True:
        for n in range(1, N):
            pt1 = Point(((n + 1 ) * 100), 100)
            pt2 = Point(((n + 1 ) * 100), (length - 100))
            ln_vert = Line(pt1, pt2)
            ln_vert.setOutline(color_rgb(0, 0, 0))
            ln_vert.setWidth(5)
            ln_vert.draw(win)

            pt3 = Point(100, ((n + 1 ) * 100))
            pt4 = Point((length - 100),((n + 1 ) * 100))
            ln_horiz = Line(pt3, pt4)
            ln_horiz.setOutline(color_rgb(0, 0, 0))
            ln_horiz.setWidth(5)
            ln_horiz.draw(win)

        else:
            break

# function for playing the game and defining the winner
def tic_tac_toe():

    # create an empty N by N matrix to track moves
    grid = [0] * N
    for row in range(N):
        grid[row] = [0] * N
    print(grid)

    # play the game until one of the conditions below is met (win or tie)
    while True:

        # record where the player 1 clicks as a coordinate
        print('Player 1 Go!')
        Player1 = win.getMouse()
        X1_Value = Player1.getX()
        Y1_Value = Player1.getY()
        print(X1_Value, Y1_Value)

        # establish which box the player clicked using the coordinates
            # if the box is taken, it's invalid and the player has one more chance to choose an empty box
            # if the box is open, replace '0' with '1' in the associated grid index and print an 'X' on the board
        for b in range(0, N):
            for a in range(0, N):
                if ((100 + 100 * a) < X1_Value < (200 + 100 * a)) and ((100 + 100 * b) < Y1_Value < (200 + 100 * b)):
                    if grid[b][a]:
                        print('Entry invalid, click an empty space otherwise forfeit your turn.')
                        print('Player 1 Go!')
                        Player1 = win.getMouse()
                        X1_Value = Player1.getX()
                        Y1_Value = Player1.getY()
                        print(X1_Value, Y1_Value)
                    else:
                        grid[b][a]
                        grid[b].pop(a)
                        grid[b].insert(a, 1)
                        print(grid)
                        Move1 = Text(Point(X1_Value, Y1_Value), "X")
                        Move1.setSize(36)
                        Move1.setTextColor(color_1)
                        Move1.draw(win)

    # Define winning criteria using lists and print who wins:
        # Check if there is a 1 in the specified index position
        # If there is, append it to the row/col/diag/rev_diag list depending on each list criteria
        # If the row/col/diag/rev_diag list has N number of 1s, X wins (ex. three in a row = three 1s)
        # Print who wins on the board, pause for 10 seconds, end the game

        # win by column
        for f in range (0, N):
            col1 = []
            for e in range (0, N):
                if grid[e][f] == 1:
                    col1.append(1)
                    print(col1)
            if col1 == ([1] * N):
                win1.draw(win)
                print('Player 1 Wins!')
                sleep(10)
                sys.exit('The game is over!')

        # win by row
        for f in range (0, N):
            row1 = []
            for e in range (0, N):
                if grid[f][e] == 1:
                    row1.append(1)
            if row1 == ([1] * N):
                win1.draw(win)
                print('Player 1 Wins!')
                sleep(10)
                sys.exit('The game is over!')

        # win by diagonal
        diag1 = []
        for g in range(0, N):
            if grid[g][g] == 1:
                diag1.append(1)
            if diag1 == ([1] * N):
                win1.draw(win)
                print('Player 1 Wins!')
                sleep(10)
                sys.exit('The game is over!')

        # win by reverse diagonal
        rev_diag1 = []
        for g in range(0, N):
            if grid[g][N - 1 - g] == 1:
                rev_diag1.append(1)
            if rev_diag1 == ([1] * N):
                win1.draw(win)
                print('Player 1 Wins!')
                sleep(10)
                sys.exit('The game is over!')


        # establish a tie by summing the grid
        if sum(map(sum, grid)) == ((N*N/2)*3)-0.5:
            break


        # Repeat the above steps for player 2: replace player 1 with player 2,
            # replace 'X' with 'O', and replace '1' with '2'

        print('Player 2 Go!')
        Player2 = win.getMouse()
        X2_Value = Player2.getX()
        Y2_Value = Player2.getY()
        print(X2_Value, Y2_Value)

        Move2 = Text(Point(X2_Value, Y2_Value), "O")
        Move2.setSize(36)
        Move2.setTextColor(color_2)
        Move2.draw(win)

        for d in range(0, N):
            for c in range(0, N):
                if ((100 + 100 * c) < X2_Value < (200 + 100 * c)) and ((100 + 100 * d) < Y2_Value < (200 + 100 * d)):
                    if grid[d][c]:
                        print('Entry invalid, click an empty space otherwise forfeit your turn.')
                        print('Player 2 Go!')
                        Player2 = win.getMouse()
                        X2_Value = Player2.getX()
                        Y2_Value = Player2.getY()
                        print(X2_Value, Y2_Value)

                    else:
                        grid[d][c]
                        grid[d].pop(c)
                        grid[d].insert(c, 2)
                        print(grid)
                        Move1 = Text(Point(X2_Value, Y2_Value), "O")
                        Move1.setSize(36)
                        Move1.setTextColor(color_2)
                        Move1.draw(win)

        # win by column
        for f in range (0, N):
            col2 = []
            for e in range (0, N):
                if grid[e][f] == 2:
                    col2.append(2)
                    print(col2)
            if col2 == ([2] * N):
                win2.draw(win)
                print('Player 2 Wins!')
                sleep(10)
                sys.exit('The game is over!')

        # win by row
        for f in range (0, N):
            row2 = []
            for e in range (0, N):
                if grid[f][e] == 2:
                    row2.append(2)
            if row2 == ([2] * N):
                win2.draw(win)
                print('Player 2 Wins!')
                sleep(10)
                sys.exit('The game is over!')


        # win by diagonal
        diag2 = []
        for g in range(0, N):
            if grid[g][g] == 2:
                diag2.append(2)
            if diag2 == ([2] * N):
                win2.draw(win)
                print('Player 2 Wins!')
                sleep(10)
                sys.exit('The game is over!')

        # win by reverse diagonal
        rev_diag2 = []
        for g in range(0, N):
            if grid[g][N - 1 - g] == 2:
                    rev_diag2.append(2)
            if rev_diag2 == ([2] * N):
                win2.draw(win)
                print('Player 2 Wins!')
                sleep(10)
                sys.exit('The game is over!')

        # tie
        if sum(map(sum, grid)) == ((N*N/2)*3):
            break

    # if there is a tie, print the tie on the board, pause for 10 seconds, end the game
    tie.draw(win)
    print("Oops, it's a tie...")
    sleep(10)
    sys.exit('The game is over!')


board()
tic_tac_toe()
