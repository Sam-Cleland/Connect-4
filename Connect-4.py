7# -*- coding: utf-8 -*-
"""
PHYS208 Assignment 1 - Connect Four
Date Created: 19/02/2018
Last Updated: 02/07/2021

A program that plays a standard game of 6x7 connect four using standard rules.
The program takes player input and plays against a computer that will make
decisions on the best move to make.

Instructions:
    - Type the integer of the column you would like to select.
    - When game is over. Message will be displayed at the top of the plot with
      the winner.
    - Type 'y' or 'n' when asked if you want to play again.
"""

import numpy as np # Contains n-directional arrays
import random as rd # Contains the randint function
from matplotlib import pyplot as plt # Contains functions for plotting

ROW_COUNT = 6 # Number of rows on the board
COLUMN_COUNT = 7 # Number of columns on the board

def create_board():
    """Creates and returns a game board made from a 6x7 numpy array."""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT)) # Creates board array of zeroes
    plot_board(board) # Plots the original empty game board
    return board 

def player_selection(board):
    """Finds which player is active. Then asks for their input and returns their...
    selected column."""
    if TURN == 0: # If player turn asks for player input
        good = False # Flase untill input is confirmed as valid
        while not good: # Loops until valid input
            col = int(input("Player make your move (1-7): ")) - 1 # Asks for player 1 input
            if (col >= 0 and col <= 6) and (check_column(board, col) is True): # Checks in range of baord and if column is not full
                good = True # If valid stops the loop
            else:
                print("Not A Valid Selection. Please Select A Valid Column") # message to user to select another columnmif invalid input
    else:
        col = computer(board) # Asks the computer for its input
    return col # returns the chosen column

def check_column(board, col):
    """Checks the given column to see if it is full. Returns boolean."""
    if board[5][col] == 0: # Checks top spot return True if empty  
         return True  

def next_open(board, col):
    """Iterates through the selected column to find the next open row. Returns...
    the value of the first open row."""
    for num in range(6): # Iterates through the column
        if board[num][col] == 0: # Checks to see if position is full
            return num

def computer(board):
    """The computer will go through a series of decisions to decide the best move...
    and return its selected column."""
    tup3 = check_three(board, piece = 1) # Checks for any three consecutive opponent pieces and blocks
    tup4 = check_three(board, piece = 2) # Checks for any three consecutive pieces and places 
    tup = check_two(board, piece = 1) # Checks for any two consecutive opponent pieces 
    tup2 = check_two(board, piece = 2) # Checks for any two consecutive pieces and places
    if board[0][3] == 0 or board[1][3]== 0: # Fills the first two center positions if availble
        col = 3
    elif tup3[0] is True: # If true will return the selected column
        col = tup3[1]
    elif tup4[0] is True:
        col = tup4[1]
    elif tup2[0] is True:
        col = tup2[1]
    elif tup[0] is True:
        col = tup[1]
    else:
        col = rd.randint(0, COLUMN_COUNT - 1) # No smart option will choose a random int
    if not check_column(board, col): # Checks the computers choice is valid
        good = False # If not a valid choice
        while not good: # Continue to ask for random int untill a valid column is chosen
            col = rd.randint(0, COLUMN_COUNT) # selects random column
            good = check_column(board, col) # checks if valid        
    return col
        
def check_two(board, piece):
    """Helper function for computer. Checks the board to find any two consecutive...
    pieces of the given piece and returns the column number for next position if empty."""
    # Check horizontal location
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3): # Iterates through the positions where a horizonatl line could start
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == 0: # Checks for any horizontal pieces 
                return (True, c + 2)
    # Checks vertical location
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT): # Iterates through the positions where a vertical line could start
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == 0: # Checks for any vertical pieces
                return (True, c)
    # Checks positive slope diagonals
    for r in range(ROW_COUNT - 4):
        for c in range(COLUMN_COUNT - 3): # Iterates through the positions where a positive diagonal line could start
            if board[r][c] == piece and board[r + 1][c + 1] and board[r + 2][c + 3] == 0: # Checks for diagonal pieces
                return (True, c + 2)
    # Checks negative slope diagonals
    for r in range(ROW_COUNT - 4):
        for c in range(COLUMN_COUNT - 4, COLUMN_COUNT): # Iterates through the positions where a negative diagonal could start
            if board[r][c] == piece and board[r + 1][c - 1] and board[r + 2][c - 3] == 0: # Checks for diagonal pieces
                return (True, c - 2)
    return (False, 0)

def check_three(board, piece):  
    """Helper fuction for computer. Checks the board to find any three consecutive...
    pieces of the given piece and returns the column number for the previous...
    position if empty."""
    # Check horizontal location 
    for r in range(ROW_COUNT):
        for c in range(1, COLUMN_COUNT - 3): # Iterates through the positions where a horizontal line could start
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c - 1] == 0:
                return (True, c - 1)
    # Checks vertical location
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT): # Iterates through the positions where a vertical line could start
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == 0:
                return (True, c)
    # Checks positive slope diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3): # Iterates through the positions where a positive diagonal line could start
            if board[r][c] == piece and board[r + 1][c + 1] and board[r + 2][c + 3] == piece and board[r -1][c - 1] == 0:
                return (True, c - 1)
    # Checks negative slope diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(3, COLUMN_COUNT): # Iterates through the positions where a negative diagonal line could start
            if board[r][c] == piece and board[r + 1][c - 1] and board[r + 2][c - 2] == piece and board[r + 1][c - 1] == 0:
                return (True, c - 1)
    return (False, 0)

def drop_row(board, col, num):
    """Takes the player selected column and row number from next_open() and places...
    the players piece in that position."""
    global DRAW
    DRAW = DRAW + 1 # Adds to conter when a position is filled
    player = player_active() # Get the piece for the selected player
    board[num][col] = player # Places the game piece for respective player
    if player == 2:
        plot_board(board) # plots the updated game board
    
def player_active():
    """Returns the current player from the TURN."""
    if TURN == 0:
        return 1 # Returns 1 if player is active 
    else:
        return 2 # Returns 2 if computer is active
    
def check_won(board): 
    """Checks the board to see if the active player has any four consecutive...
    pieces. Returns boolean."""
    piece = player_active()
    # Check horizontal location
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                x, y = [c+1,c+2,c+3,c+4], [r+1,r+1,r+1,r+1]
                victory(board, x, y) # plot the line of the winning play
                return True
    # Checks vertical location
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:     
                x, y = [c+1,c+1,c+1,c+1], [r+1,r+2,r+3,r+4]
                victory(board, x, y) # plot the line of the winning play
                return True
    # Checks positive slope diagonals
    for r in range(ROW_COUNT - 4):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                x, y = [c+1,c+2,c+3,c+4], [r+1, r+2, r+3, r+4]
                victory(board, x, y) # plot the line of the winning play
                return True
    # Checks negative slope diagonals
    for r in range(ROW_COUNT - 4):
        for c in range(3, COLUMN_COUNT):
            if board[r][c] == piece and board[r + 1][c - 1] == piece and board[r + 2][c - 2] == piece and board[r + 3][c - 3] == piece:
                x, y = [c+1, c, c-1, c-2], [r+1,r+2,r+3,r+4]
                victory(board, x, y) # plot the line of the winning play
                return True
    if DRAW == 42: # If true the board is full and game is a draw
        victory(board)
        return True
               
def plot_board(board, x = [], y = [], title = "--Connect Four--"):
    "Plots the game board."
    plt.xkcd()
    x1 = [] # Sets a list of each players piece positions on the board.
    y1 = []
    x2 = []
    y2 = []
    for r in range(ROW_COUNT):  # Iterates through the board to find position of each players pieces.
        for c in range(COLUMN_COUNT):
            if board[r][c] == 1: # Finds and logs players selections
                x1.append(c + 1)
                y1.append(r + 1)
            if board[r][c] == 2: # Finds and logs computer selections
                x2.append(c + 1)
                y2.append(r + 1)
    xbase, ybase = [1,2,3,4,5,6,7], [1,2,3,4,5,6] # Sets x and y data for ticks
    plt.plot(x1, y1, marker='o', color='red', markersize=20, linestyle = 'None') # Plots the players pieces in red
    plt.plot(x2, y2, marker='o', color='yellow', markersize=20, linestyle = 'None') # Plots the computer pieces in yellow
    plt.plot(x, y, linewidth=5, color='black') # Plots the line of winning move. By defeault with plot nothing
    axes = plt.gca() # Get axes 
    plt.title(title) # Plot title and axes labels
    plt.xlabel("Column (1-7)")
    plt.ylabel("Row (1-6)")
    xtick, ytick = [1,2,3,4,5,6,7], [1,2,3,4,5,6] # lists of wanted ticks
    plt.xticks(xbase, xtick) # sets the ticks for each axes 
    plt.yticks(ybase, ytick)
    axes.set_xlim(0, 8) # Sets the axes to the size of the gameboard
    axes.set_ylim(0, 7)
    axes.grid() # Creates a grid on the plot
    axes.xaxis.grid(linewidth=1.3) # Sets the linewidth so that gridlines are visible
    axes.yaxis.grid(linewidth=1.3)
    plt.show() # Shows the plot
             
def victory(board, x, y):
    global TURN
    if DRAW == 42: # The game is a draw
        plot_board(board, x, y, title = "!Draw!" )
    elif TURN == 0: # The player has waon
        plot_board(board, x, y, title = "!Congratulations Player!")
    else: # the computer has won
        plot_board(board, x, y, title = "!Computer Wins!")
        
def main():
    """Runs the game."""
    board = create_board()
    game = False # Sets status of game
    while not game: # Runs untill game is won
        col = player_selection(board) # Asks player for selected column
        num = next_open(board, col) # Finds num of next open row
        drop_row(board, col, num) # Places the piece in the bpoard
        game = check_won(board) # Checks to see if the game is won
        global TURN
        TURN = (TURN + 1) % 2 # Alternates turn between 0 - 1

# This section resets counters and decides whether to play again based on player input     
cont = 'y' # Sets the initial game as yes
while cont.lower() in ['yes', 'y']: # Continues looping the game as player continues to play again
    global TURN, DRAW
    TURN = 0 # Sets turn counter for each game
    DRAW = 0 # Sets the draw counter for each game
    main() # plays the game
    cont = input("Play Again (y/n): ") # Asks if player would like to play again
print('')
print("Thanks For Playing :)") # Prints leaving message 