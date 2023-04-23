import unittest
from sudoku_solver import Board

def test_Board_init():
    """ Test whether __init__() method works as expected """

    # create an instance
    board = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 0, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]]
    new_board = Board(board)

    # check for expected attributes
    for attr, val in [("board", board)]:
        assert hasattr(new_board, attr), \
            f"instance of Book class has no {repr(attr)} attribute"
        assert getattr(new_board, attr) == val, \
            f"unexpected value for {repr(attr)} attribute"

def test_Board_solver():
    """ Test whether the solve_board() method wors as expected """

    # create an instance
    board = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 0, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]]
    solution = [[2, 5, 8, 7, 3, 6, 9, 4, 1],
                [6, 1, 9, 8, 2, 4, 3, 5, 7],
                [4, 3, 7, 9, 1, 5, 2, 6, 8],
                [3, 9, 5, 2, 7, 1, 4, 8, 6],
                [7, 6, 2, 4, 9, 8, 1, 3, 5],
                [8, 4, 1, 6, 5, 3, 7, 2, 9],
                [1, 8, 4, 3, 6, 9, 5, 7, 2],
                [5, 7, 6, 1, 4, 2, 8, 9, 3],
                [9, 2, 3, 5, 8, 7, 6, 1, 4]]
    new_board = Board(board)

    new_board.solve_board(0, 0)

    assert new_board.board == solution






