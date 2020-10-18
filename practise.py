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
    print(row_blank)
    print(col_blank)

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
    Havent decided yet on which heuristic to use 
    """
    pass


def aStar(self, goalState, heuristic, output):
    """ 
    Takes in the the currentState of the puzzle and solves it.
    Returns: 
        - numSteps : number of steps to find solution. Essentially the number of times we call result()
        - nodesExtended : number of states explored. Essentially the number of times we call the heuristic() 
    """

    closed_set = set()      
    open_set = set([self])
    
    #the prev node
    came_from = {}
        
    #current node depth
    g_score = {self : 0}
    #calculating cost for current node
    f_score = {self : g_score[self] + heuristic(self, goalState)}
        
    while (len(open_set) != 0):
#           print len(open_set),len(closed_set)
        current = None
        for node in open_set:
            if current is None or f_score[node] < f_score[current]:
                current = node
        if current == goal:
            return output(self, came_from, current)
                
        open_set.remove(current)
        closed_set.add(current)


        for n in current.actions():
            neighbor = n[0]
#                print "Neighbor:\n",neighbor
            if neighbor in closed_set:
#                    print "Current:\n",current
#                    print "Neighbor:\n",neighbor
                continue
            tentative_g_score = g_score[current] + 1
                
            if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = (current, n[1])
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor,goal)
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return "nil"

