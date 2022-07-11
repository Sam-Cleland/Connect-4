# -*- coding: utf-8 -*-
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

import numpy as np
import random as rd 
from matplotlib import pyplot as plt


def create_board():
    """Creates and returns an empty game board made from a 6x7 numpy array."""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT)) 
    plot_board(board) 
    return board 


def player_selection(board):
    """Finds which player is active. Then asks for their input and returns their...
    selected column."""
    if TURN == 0: 
        good = False 
        while not good: 
            col = int(input("Player make your move (1-7): ")) - 1 # Asks player input
            if (col >= 0 and col <= 6) and (check_column(board, col) is True): 
                good = True 
            else:
                print("Not A Valid Selection. Please Select A Valid Column") 
    else:
        col = computer(board) # gets computer input
    return col 


def check_column(board, col):
    """Checks the given column to see if it is full. Returns boolean."""
    if board[5][col] == 0:  
         return True  


def next_open(board, col):
    """Iterates through the selected column to find the next open row. Returns...
    the value of the first open row."""
    for num in range(6): 
        if board[num][col] == 0: 
            return num
        
        
def computer(board):
    """The computer will go through a series of decisions to decide the best move...
    and return its selected column."""
    tup3 = check_three(board, piece = 1) 
    tup4 = check_three(board, piece = 2) 
    tup = check_two(board, piece = 1) 
    tup2 = check_two(board, piece = 2) 
    if board[0][3] == 0 or board[1][3]== 0:
        col = 3
    elif tup3[0] is True: 
        col = tup3[1]
    elif tup4[0] is True:
        col = tup4[1]
    elif tup2[0] is True:
        col = tup2[1]
    elif tup[0] is True:
        col = tup[1]
    else:
        col = rd.randint(0, COLUMN_COUNT - 1) 
    if not check_column(board, col): 
        good = False 
        while not good: 
            col = rd.randint(0, COLUMN_COUNT) 
            good = check_column(board, col)      
    return col


def check_two(board, piece):
    """Helper function for computer. Checks the board to find any two consecutive...
    pieces of the given piece and returns the column number for next position if empty."""
    # Check horizontal location
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3): 
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == 0: 
                return (True, c + 2)
    # Checks vertical location
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT): 
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == 0: 
                return (True, c)
    # Checks positive slope diagonals
    for r in range(ROW_COUNT - 4):
        for c in range(COLUMN_COUNT - 3): 
            if board[r][c] == piece and board[r + 1][c + 1] and board[r + 2][c + 3] == 0: 
                return (True, c + 2)
    # Checks negative slope diagonals
    for r in range(ROW_COUNT - 4):
        for c in range(COLUMN_COUNT - 4, COLUMN_COUNT): 
            if board[r][c] == piece and board[r + 1][c - 1] and board[r + 2][c - 3] == 0: 
                return (True, c - 2)
    return (False, 0)


def check_three(board, piece):  
    """Helper fuction for computer. Checks the board to find any three consecutive...
    pieces of the given piece and returns the column number for the previous...
    position if empty."""
    # Check horizontal location 
    for r in range(ROW_COUNT):
        for c in range(1, COLUMN_COUNT - 3): 
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c - 1] == 0:
                return (True, c - 1)
    # Checks vertical location
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT): 
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == 0:
                return (True, c)
    # Checks positive slope diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3): 
            if board[r][c] == piece and board[r + 1][c + 1] and board[r + 2][c + 3] == piece and board[r -1][c - 1] == 0:
                return (True, c - 1)
    # Checks negative slope diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(3, COLUMN_COUNT): 
            if board[r][c] == piece and board[r + 1][c - 1] and board[r + 2][c - 2] == piece and board[r + 1][c - 1] == 0:
                return (True, c - 1)
    return (False, 0)


def drop_row(board, col, num):
    """Takes the player selected column and row number from next_open() and places...
    the players piece in that position."""
    global DRAW
    DRAW = DRAW + 1 
    player = player_active() 
    board[num][col] = player 
    if player == 2:
        plot_board(board) 
    
    
def player_active():
    """Returns the current player from the TURN."""
    if TURN == 0:
        return 1 
    else:
        return 2 
    
    
def check_won(board): 
    """Checks the board to see if the active player has any four consecutive...
    pieces. Returns boolean."""
    piece = player_active()
    # Check horizontal location
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                x, y = [c+1,c+2,c+3,c+4], [r+1,r+1,r+1,r+1]
                victory(board, x, y) 
                return True
    # Checks vertical location
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:     
                x, y = [c+1,c+1,c+1,c+1], [r+1,r+2,r+3,r+4]
                victory(board, x, y) 
                return True
    # Checks positive slope diagonals
    for r in range(ROW_COUNT - 4):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                x, y = [c+1,c+2,c+3,c+4], [r+1, r+2, r+3, r+4]
                victory(board, x, y) 
                return True
    # Checks negative slope diagonals
    for r in range(ROW_COUNT - 4):
        for c in range(3, COLUMN_COUNT):
            if board[r][c] == piece and board[r + 1][c - 1] == piece and board[r + 2][c - 2] == piece and board[r + 3][c - 3] == piece:
                x, y = [c+1, c, c-1, c-2], [r+1,r+2,r+3,r+4]
                victory(board, x, y) 
                return True
    if DRAW == 42: 
        victory(board)
        return True
   
   
def plot_board(board, x = [], y = [], title = "--Connect Four--"):
    "Plots the game board."
    plt.xkcd()
    x1 = [] 
    y1 = []
    x2 = []
    y2 = []
    for r in range(ROW_COUNT): 
        for c in range(COLUMN_COUNT):
            if board[r][c] == 1: 
                x1.append(c + 1)
                y1.append(r + 1)
            if board[r][c] == 2: 
                x2.append(c + 1)
                y2.append(r + 1)
    xbase, ybase = [1,2,3,4,5,6,7], [1,2,3,4,5,6] 
    plt.plot(x1, y1, marker='o', color='red', markersize=20, linestyle = 'None') 
    plt.plot(x2, y2, marker='o', color='yellow', markersize=20, linestyle = 'None') 
    plt.plot(x, y, linewidth=5, color='black') 
    axes = plt.gca() 
    plt.title(title) 
    plt.xlabel("Column (1-7)")
    plt.ylabel("Row (1-6)")
    xtick, ytick = [1,2,3,4,5,6,7], [1,2,3,4,5,6] 
    plt.xticks(xbase, xtick)
    plt.yticks(ybase, ytick)
    axes.set_xlim(0, 8) 
    axes.set_ylim(0, 7)
    axes.grid() 
    axes.xaxis.grid(linewidth=1.3) 
    axes.yaxis.grid(linewidth=1.3)
    plt.show() 
        
        
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
    global TURN, DRAW, ROW_COUNT, COLUMN_COUNT
    cont = 'y'
    while cont.lower() in ['yes', 'y']: 
        TURN = 0 
        DRAW = 0
        ROW_COUNT = 6
        COLUMN_COUNT = 7
        board = create_board()
        game = False 
        while not game: 
            col = player_selection(board) 
            num = next_open(board, col) 
            drop_row(board, col, num) 
            game = check_won(board) 
            TURN = (TURN + 1) % 2
        cont = input("Play Again (y/n): ")
    print('')
    print("Thanks For Playing :)") 

if __name__ == '__main__':
    main()