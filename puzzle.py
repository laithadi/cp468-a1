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
            [7, 8, 0]
        ]

    elif size == 15:
        goalState = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]

    else:
        goalState = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 0]
        ]

    return goalState


def initialState(size):
    """
    Returns the initial state of the puzzle 
    """
    if size == 8:
        arr = np.arange(9).reshape(3, 3)
        arr = np.where(arr == 0, 0, arr)
        arr = arr.ravel()
        np.random.shuffle(arr)
        arr = arr.reshape(3,3)
        arr = arr.tolist()

    elif size == 15:
        arr = np.arange(16).reshape(4, 4)
        arr = np.where(arr == 0, 0, arr)
        arr = arr. ravel()
        np.random.shuffle(arr)
        arr = arr.reshape(4,4)
        arr = arr.tolist()
    else:
        arr = np.arange(25).reshape(5, 5)
        arr = np.where(arr == 0, 0, arr)
        arr = arr.ravel()
        np.random.shuffle(arr)
        arr = arr.reshape(5,5)
        arr = arr.tolist()
    return arr


def inversion(puzzle):
    """
    Gets the inversion of the puzzle
    """
    
    size = len(puzzle)
    inv_count = 0

    for i in range(0, size - 1):
        for j in range(1+i, size - 1):
            if puzzle[j][i] > 0 and puzzle[j][i] > puzzle[i][j]:
                inv_count += 1 

    return inv_count


def XPos(puzzle):
    """
    gets the position of the blank spot from the bottom 
    """
    size = len(puzzle)
    for i in range(size-1, -1, -1):
        for j in range(size-1, -1, -1):
            if puzzle[i][j] == 0:
                return size - i 


def is_puzzle_solvable(puzzle):
    """ 
    Check if the puzzle is solvable or not. 
    """

    inv_count = inversion(puzzle)
    size = len(puzzle) 

    if size%2 == 0:

        if inv_count % 2 == 0:
            return False 
        else:
            return True  
    
    else:

        blank = XPos(puzzle)
        if blank%2 == 0:
            if inv_count % 2 == 2:
                return False 
            else:
                return True 
        else:
            if inv_count % 2 == 0:
                return True
            else:
                return False 


def blankSpot(puzzle):
    """
    returns the indix (i, j) of where the blank spot is 
    """
    temp = copy.deepcopy(puzzle)
    length = len(temp)

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


def get_index(array, value):

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == value:
                return (i, j)
    return -1, -1


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
            if currentState[i][j] != 0:
                if (currentState[i][j] != goalState[i][j]):
                    misplacedTiles += 1

    return misplacedTiles


def h2(currentState, goalState):
    """
    Manhatton Distance
    """
    length = len(currentState)
    manhatton = 0

    for x in range(length):
        for y in range(length):
            #to ignore the empty tile
            if currentState[x][y] != 0 or currentState[x][y] != 0:
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


def aStar(currentState, goalState, heuristic):
    """ 
    Takes in the the currentState of the puzzle and solves it.
    Returns: 
        - numSteps : number of steps to find solution. Essentially the number of times we call result()
        - nodesExtended : number of states explored. Essentially the number of times we call the heuristic() 
    """
    

    curr_state = copy.deepcopy(currentState)
    goal_state = copy.deepcopy(goalState) 

    queue = [] 
    visited = []

    g_score = 0 
    nodes_expanded = 0 

    queue.append((99999, curr_state))
    visited.append(curr_state)

    diction = {}
    diction[999999] = curr_state 

    while len(diction) != 0:
        g_score += 1
        # print(curr_state)
        # print()
        if puzzleSolved(curr_state, goal_state): return g_score, nodes_expanded
        acts = actions(curr_state)

        for act in acts:
            res_act = result(curr_state, act) 
            if puzzleSolved(res_act, goal_state): return g_score, nodes_expanded
        
            nodes_expanded += 1

            if heuristic == 'h1':
                res_act_score = int(g_score + h1(res_act, goal_state))
            elif heuristic == 'h2': 
                res_act_score = int(g_score + h2(res_act, goal_state))
            else:
                res_act_score = int(g_score + h3(res_act, goal_state))
            # queue.append((res_act_score, res_act))

            if res_act not in visited:
                visited.append(res_act)
                diction[res_act_score] = res_act
            # queue.sort(key=lambda x:x[0], reverse=True)


        temp = sorted(diction.keys())

        curr_state = diction[temp[0]]

        del diction[temp[0]]

        # temp = queue.pop()
        # temp = diction.pop()
        # curr_state = temp[1] 
        # print(curr_state)

    return 0000, 0000
































    # curr_state = copy.deepcopy(currentState)
    # goal_state = copy.deepcopy(goalState) 

    # visited = set()

    # g_score = 0 
    # nodes_expanded = 0 

    # if heuristic == 'h1':
    #     curr_state_score = int(g_score + h1(curr_state, goal_state))
    # elif heuristic == 'h2': 
    #     curr_state_score = int(g_score + h2(curr_state, goal_state))
    # else:
    #     curr_state_score = int(g_score + h3(curr_state, goal_state))

    # frontier = {}
    # frontier[curr_state_score] = curr_state

    # # frontier = [] 
    # # frontier.append(curr_state, 999)
    # cost_so_far = {}
    # cost_so_far[curr_state_score] = curr_state
    # total = 0
    # while frontier:

    #     temp = sorted(frontier.keys(), reverse=True)

    #     next_state = frontier[temp[0]]

    #     curr_state = next_state

    #     # del frontier[temp[0]]
        
    #     print(curr_state)

    #     if puzzleSolved(curr_state, goal_state): return g_score, nodes_expanded


    #     acts = actions(curr_state)

        

    #     for act in acts:
    #         res_act = result(curr_state, act)
    #         nodes_expanded += 1

    #         if heuristic == 'h1':
    #             res_act_score = int(g_score + h1(res_act, goal_state))
    #         elif heuristic == 'h2': 
    #             res_act_score = int(g_score + h2(res_act, goal_state))
    #         else:
    #             res_act_score = int(g_score + h3(res_act, goal_state))
            
    #         total += res_act_score

    #         if res_act not in visited or res_act_score < total: 
    #             visited.add(res_act)
    #             frontier[res_act_score] = res_act
    
    

    # return 0000, 0000