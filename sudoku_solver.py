"""
Name: Rebecca Zhang
Directory ID: rzhang10
Date: 2022-12-08
Assignment: Final Project
"""

import sys
from argparse import ArgumentParser
import math
import re

class Board:
    """ Class that represents a sudoku board. 

    This class can be used to create a sudoku board and solve that board 
    or return false if the board can not be solved. Using a 2-D and 
    backtracking algorithm, the solution (if there is one) is found. 
    The original boar dis overwritten when looing for the solution.
    This class also provides a way to print out the board whether it is 
    the solution acurrent board.

    Attributes:
        board (list of list of ints): current arrangment of sudou board
        length (int): the length/width of the board
    """

    def __init__(self, board):
        self.board = board
        self.length = 9

    def works(self, row, col, num):
        """ Checks if the number provided can be placed in that square.

        Looking at the rest of the board, checks if the row, column or
        square has the number provided already. If there is, false is
        returned because the number can not be placed there. Otherwise,
        true is returned.

        Args:
            row (int): the row that the number is going in
            col (int): the col that the number is going in
            nun (int): the number to test in that location

        Returns:
            bool: whether that number can be placed there
        """

        length_box = 3
        box_row = row - (row % length_box)
        box_col = col - (col % length_box)

        for curr_row in range(box_row, box_row + length_box):
            for curr_col in range(box_col, box_col + length_box):
                if (self.board[curr_row][curr_col] == num):
                    return False

        for curr_row in range(self.length):
            if (self.board[curr_row][col] == num):
                return False
            
        for curr_col in range(self.length):
            if (self.board[row][curr_col] == num):
                return False

        return True

    def solve_board(self, row, col):
        """ Solved the sudoku board.

        Using a backtracking algorithm, the solution of the 
        sudoku baord is found. If checks to make sure the 
        location is valid and starts to plug in numbers. 
        With each number, the number is checked to make 
        sure it can go there, otherwise we backtrack and
        test a different number, The return is whether a 
        valid solution was found.

        Args:
            row (int): the row that the number is going in
            col (int): the col that the number is going in

        Returns:
            bool: whether a solutions was found for the 
                    board
        """
        if (row == self.length - 1 and col == self.length):
            return True
        
        if col == self.length:
            row += 1
            col = 0

        if self.board[row][col] > 0:
            return self.solve_board(row, col + 1)

        for num in range(1, self.length + 1): 
            if self.works(row, col, num):
                self.board[row][col] = num

                if self.solve_board(row, col + 1):
                    return True
            
            self.board[row][col] = 0

        return False

    def __repr__(self):
        for row in range(0, self.length):
            for col in range(0, self.length):
                print(str(self.board[row][col]), end = " ")
            print()

def main():
    """ The main body for the program. 
    
    Reads in user input. Then, checks to make sure all 
    the lengths are correct for the board and then runs 
    the program with the user input.


    Side Effects:
        Prints out to stdout the user provided board 
        and then the board after if it was been 
        solved. Otherwise, prints out why the board 
        was not solved.

    """
    args = parse_args(sys.argv[1:])
    board = []

    if len(sys.argv[1:]) == 0:
    
        # need to change to regexxxx
        while True:
            try:
                line = input().strip()
            except EOFError:
                break
            row = []
            numbers = re.findall(r'\d', line)
            for num in numbers:
                row.append(num)
            board.append(row)
    else:

        with open(args.file) as f:
            for line in f:
                string = line.strip()
                row = []
                numbers = re.findall(r'\d', line)
                for num in numbers:
                    row.append(num)
                board.append(row)

    length = len(board)

    if length != 0:
        if length != 9:
            print("Not a valid number of rows")
        else:
            correct_len = True
            for lst in board:
                if len(lst) != 9:
                    correct_len = False

            if correct_len:
                num_board = []
                for lst in board:
                    row = []
                    for num in lst:
                        row.append(int(num))
                    num_board.append(row)

                new_board = Board(num_board)
                print("Original:")
                new_board.__repr__()
                print()

                if (new_board.solve_board(0, 0)):
                    print("Solution:")
                    new_board.__repr__()
                else:
                    print("Can not be solved")
            else:
                print("Incorrect number of columns")
    else:
        print("No input was provided")

def parse_args(arglist):
    """Parse and validate command-line arguments.

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)
    """
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", 
                        help= "path to a file with a sudoku board")

    return parser.parse_args(arglist)

if __name__ == "__main__":
    main()
        


