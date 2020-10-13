import copy
import random
import numpy as np
import math


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
    # Exception has occurred: ValueError
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


def result(puzzle, act):
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


def get_index(array, value):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == value:
                return (i, j)
    return -1, -1


def h2(currentState, goalState):
    """
    Manhatton Distance
    """
    length = len(currentState)
    manhatton = 0

    for x in range(length):
        for y in range(length):
            (goalx, goaly) = get_index(goalState, currentState[x][y])
            manhatton += abs(x - goalx) + abs(y - goaly)

    return manhatton


def h3(currentState, goalState):
    """
    Euclidean Distance
    """
    length = len(currentState)
    euclidean = 0
    for x in range(length):
        for y in range(length):
            (goalx, goaly) = get_index(goalState, currentState[x][y])
            euclidean += math.sqrt((x-y)**(2) + (goalx - goaly)**(2))

    return euclidean


def aStar(currentState, goalState, max_num, heuri):
    """ 
    Takes in the the currentState of the puzzle and solves it.
    Returns: 
        - numSteps : number of steps to find solution. Essentially the number of times we call result()
        - nodesExtended : number of states explored. Essentially the number of times we call the heuristic() 
    """

    # first thing: deepcopy the current state, and goalstate
    # gn = 1 
    # second thing: while loop for when the puzzlesolved() is false 
        # actions(current state ) 
        # result() for each action so we can get the next state/children 
        # calculate the cost (g(n) + h(n)) 
        # order the different states (options) least to greatest based off of their costs 
        # pick the least cost state 
        # set the current state to the state that we chose in above step 
        # we want check if the puzzle is solved, and if it is not then we go back to the top of loop 
        # gn += 1 
    
    curr_state= copy.deepcopy(currentState)
    goal_state= copy.deepcopy(goalState)

    count= 1

    closed_set = set()      
    open_set = set([self])
    
    #current node depth
    g_score = {self : 0}
    #calculating cost for current node
    f_score = {self : g_score[self] + heuristic(self, goal_state)}

    #the prev node
    came_from = {}

    while (len(open_set) != 0) and puzzleSolved != True:

        curr= None
        for n in open_set:
            if 
        

    pass
