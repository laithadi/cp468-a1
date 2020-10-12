import copy
import random
import numpy as np


def goalState(size):
    """
    depending on the size, the goal state is longer/shorter
    """
    if size == 8:
        goalState = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, None]
        ]

    elif size == 15:
        goalState = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, None]
        ]

    else:
        goalState = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, None]
        ]

    return goalState


def initialState(size):
    """
    Returns the initial state of the puzzle 
    """
    if size == 8:
        arr = np.arange(9).reshape(3, 3)
        np.random.shuffle(arr)
    elif size == 15:
        arr = np.arange(16).reshape(4, 4)
        np.random.shuffle(arr)
    else:
        arr = np.arange(25).reshape(5, 5)
        np.random.shuffle(arr)
    return arr


def blankSpot(puzzle):
    """
    returns the indix (i, j) of where the blank spot is 
    """
    temp = copy.deepcopy(puzzle)
    length = len(temp) - 1

    for i in range(0, length):
        for j in range(0, length):
            if temp[i][j] == 0:
                return i, j

    return temp

def actions(puzzle):
    """
    Returns set of all possible actions available on the puzzle 
    """
    temp = copy.deepcopy(puzzle)
    length = len(temp) - 1

    acts = set()

    # find the blank spot
    rowcol = blankSpot(temp)
    row_blank, col_blank = rowcol[0], rowcol[1]

    # up
    if ((row_blank - 1) >= 0):
        acts.add((row_blank - 1, col_blank))

    # down
    if ((row_blank + 1) <= length):
        acts.add((row_blank + 1, col_blank))

    # right
    if ((col_blank + 1) <= length):
        acts.add((row_blank, col_blank + 1))

    # left
    if ((col_blank - 1) >= 0):
        acts.add((row_blank, col_blank - 1))

    return acts


def result(puzzle, act, blank):
    """
    Takes in the action (move) and does it on the puzzle. 
    -------------------------------------------------------
    Parameters:
        puzzle: the puzzle state that the act is to be done on 
        act: a tuple (i, j) with the coordinates (indix) of the sport we can switch with the blank spot 
        blank: where the blank spot is in the puzzle  (i, j)
    Return: 
        puzzle state after moving the blank spot to the act 
    """

    temp = copy.deepcopy(puzzle)

    row0 = act[0]
    col0 = act[1]
    rowcol = blankSpot(temp)
    row1, col1 = rowcol[0], rowcol[1]

    numAct = temp[row0][col0]
    blank1 = temp[row1][col1]

    temp[row0][col0] = blank1
    temp[row1][col1] = numAct

    return temp


def h1(currentState, goalState):
    """
    Takes current state and goal state of puzzle. Then calculates the number of misplaced tiles. 
    ---------------------------------------------------------------------------------------------
    Parameteres:
        currentState: current state of the puzzle 
        goalState: goal state of the puzzle we are trying to achieve 
    """

    length = len(currentState)
    misplacedTiles = 0
    for i in range(0, length):
        for j in range(0, length):
            if (currentState[i][j] != goalState[i][j]):
                misplacedTiles += 1

    return misplacedTiles


def puzzleSolved(puzzle, goalState):
    """ 
    Returns whether the puzzle is solved or not 
    """

    temp = h1(puzzle, goalState)

    if (temp == 0):
        solved = True
    else:
        solved = False

    return solved


def h2(currentState, goalState):
    """
    Manhatton Distance 
    """
    pass

def h3(currentState, goalState):
    """
    Havent decided yet on which heuristic to use 
    """
    pass

def aStar(currentState, goalState, max_num, heuri):
    """ 
    Takes in the the currentState of the puzzle and solves it.
    Returns: 
        - numSteps : number of steps to find solution. Essentially the number of times we call result()
        - nodesExtended : number of states explored. Essentially the number of times we call the heuristic() 
    """

    

    pass