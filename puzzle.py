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
        arr = np.where(arr == 0, None, arr)
        arr = arr.tolist()

    elif size == 15:
        arr = np.arange(16).reshape(4, 4)
        np.random.shuffle(arr)
        arr = np.where(arr == 0, None, arr)
        arr = arr.tolist()
    else:
        arr = np.arange(25).reshape(5, 5)
        np.random.shuffle(arr)
        arr = np.where(arr == 0, None, arr)
        arr = arr.tolist()
    return arr


def blankSpot(puzzle):
    """
    returns the indix (i, j) of where the blank spot is 
    """
    temp = copy.deepcopy(puzzle)
    length = len(temp)

    for i in range(0, length):
        for j in range(0, length):
            if temp[i][j] == None:
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
            if currentState[i][j] != None:
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
            if currentState[x][y] != None or currentState[x][y] != 0:
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

'''
def aStar(currentState, goalState, max_num, heuristic):
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
    g= 0
    h= 0 
    f= 0  
    # setting up the start nodes
    node_start= Node(None, curr_state)
    node_start.g= node_start.h = node_start.f = 0 
    
    # setting up the end nodes
    node_end= Node(Node, goal_state)
    node_end.g = node_end.h = node_end.f = 0 
    #Making the intial open and closed sets/lists
    open_set = []
    closed_set=[]
    #adding the starting node to our open set list
    open_set.append(node_start)
    #Iterating thru the list
    while len(open_set) > 0:
        #Geting the curr node 
         curr_state= open_set[0]
         count=0 
         for index, item in enumerate(open_set):
             if item.f < curr_state.f:
                 curr_state
   # pass
'''

def aStarh2(currentState, goalState, size):
    """ 
    Takes in the the currentState of the puzzle and solves it.
    Returns: 
        - numSteps : number of steps to find solution. Essentially the number of times we call result()
        - nodesExtended : number of states explored. Essentially the number of times we call the heuristic() 
    """

    # first thing: deepcopy the current state, and goalstate
    # gn = 1 
    # second thing: while loop for when the puzzlesolved() is false 
        # actions(current state) 
        # result() for each action so we can get the next state/children 
        # calculate the cost (g(n) + h(n)) 
        # order the different states (options) least to greatest based off of their costs 
        # pick the least cost state 
        # set the current state to the state that we chose in above step 
        # we want check if the puzzle is solved, and if it is not then we go back to the top of loop 
        # gn += 1 
    

    tb = {
        8 : 2,
        15: 3,
        24: 4,
    }

    #current node depth
    g_score = 0

    #calculating cost for current node
    f_score = g_score + h2(currentState, goalState)

    currentState = [copy.deepcopy(currentState), f_score, g_score]
    goalState = copy.deepcopy(goalState)

    tree = []
    
    visit= 0 

    queue= [currentState]

    while len(queue):

        currentState = queue.pop(0)
        '''
        for i in currentState[0]:
            print(i)
        print()
        '''
        tree.append(currentState[0])

        blank_pos = get_index(currentState[0], None) # get the blank tile pos, might be 0 or None

        if blank_pos == (-1, -1):
            print('There is no None in the currentState')
            blank_pos = get_index(currentState[0],0)
            return
        # add count for where ever we expanded nodes (visited children)
        g_score = currentState[2]
        
        if blank_pos[1] > 0:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0]][blank_pos[1] - 1], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0]][blank_pos[1] - 1]
            if new_node == goalState:
                # print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h2(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1
        
        if blank_pos[1] < tb[size]:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0]][blank_pos[1] + 1], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0]][blank_pos[1] + 1]
            if new_node == goalState:
                # print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h2(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1
        
        if blank_pos[0] > 0:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0] - 1][blank_pos[1]], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0] - 1][blank_pos[1]]
            if new_node == goalState:
                # print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h2(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1


        if blank_pos[0] < tb[size]:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0] + 1][blank_pos[1]], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0] + 1][blank_pos[1]]
            if new_node == goalState:
                #print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h2(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1
        
        queue.sort(key=lambda x: x[1])



def aStarh1(currentState, goalState, size):
    """ 
    h1  heuristic
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
    

    tb = {
        8 : 2,
        15: 3,
        24: 4,
    }

    #current node depth
    g_score = 0

    #calculating cost for current node
    f_score = g_score + h1(currentState, goalState)

    currentState = [copy.deepcopy(currentState), f_score, g_score]
    goalState = copy.deepcopy(goalState)

    tree = []
    
    visit= 0 

    queue= [currentState]

    while len(queue):

        currentState = queue.pop(0)
        
        #for i in currentState[0]:
        #    print(i)
        #print()
        
        tree.append(currentState[0])

        blank_pos = get_index(currentState[0], None) # get the blank tile pos, might be 0 or None

        if blank_pos == (-1, -1):
            print('There is no None in the currentState')
            blank_pos = get_index(currentState[0],0)
            return
        # add count for where ever we expanded nodes (visited children)
        g_score = currentState[2]
        
        if blank_pos[1] > 0:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0]][blank_pos[1] - 1], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0]][blank_pos[1] - 1]
            visit += 1
            if new_node == goalState:
                # print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h1(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1
        
        if blank_pos[1] < tb[size]:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0]][blank_pos[1] + 1], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0]][blank_pos[1] + 1]
            if new_node == goalState:
                # print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h1(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1
        
        if blank_pos[0] > 0:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0] - 1][blank_pos[1]], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0] - 1][blank_pos[1]]
            if new_node == goalState:
                # print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h1(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1

        if blank_pos[0] < tb[size]:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0] + 1][blank_pos[1]], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0] + 1][blank_pos[1]]
            if new_node == goalState:
                # print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit 
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h1(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1
        
        queue.sort(key=lambda x: x[1])



def aStarh3(currentState, goalState, size):
    """ 
    h3  heuristic
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
    

    tb = {
        8 : 2,
        15: 3,
        24: 4,
    }

    #current node depth
    g_score = 0

    #calculating cost for current node
    f_score = g_score + h3(currentState, goalState)

    currentState = [copy.deepcopy(currentState), f_score, g_score]
    goalState = copy.deepcopy(goalState)

    tree = []
    
    visit= 0 

    queue= [currentState]

    while len(queue):

        currentState = queue.pop(0)
        '''
        for i in currentState[0]:
            print(i)
        print()
        '''
        tree.append(currentState[0])

        blank_pos = get_index(currentState[0], None) # get the blank tile pos, might be 0 or None

        if blank_pos == (-1, -1):
            print('There is no None in the currentState')
            blank_pos = get_index(currentState[0],0)
            return
        # add count for where ever we expanded nodes (visited children)
        g_score = currentState[2]
        
        if blank_pos[1] > 0:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0]][blank_pos[1] - 1], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0]][blank_pos[1] - 1]
            visit += 1
            if new_node == goalState:
                # print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h3(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1
        
        if blank_pos[1] < tb[size]:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0]][blank_pos[1] + 1], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0]][blank_pos[1] + 1]
            if new_node == goalState:
                # print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h3(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1
        
        if blank_pos[0] > 0:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0] - 1][blank_pos[1]], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0] - 1][blank_pos[1]]
            if new_node == goalState:
                # print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h3(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1

        if blank_pos[0] < tb[size]:
            new_node = copy.deepcopy(currentState[0])
            new_node[blank_pos[0] + 1][blank_pos[1]], new_node[blank_pos[0]][blank_pos[1]] =\
                new_node[blank_pos[0]][blank_pos[1]],  new_node[blank_pos[0] + 1][blank_pos[1]]
            if new_node == goalState:
                # print(new_node)
                # print('Depth: ' + str(g_score))
                # print('Children visited: ' + str(visit))
                return g_score, visit
            if new_node not in tree: # check whether is this arrangement have already been done
                # f_score = h2(new_node, goalState) + g_score
                f_score = h3(new_node, goalState)
                queue.append([new_node, f_score, g_score + 1])
                visit += 1
        
        queue.sort(key=lambda x: x[1])
    


# if __name__ == '__main__':
#     import time
#     result = aStar([[2, 1, 5, 8], [6, None, 4, 11], [9, 7, 3, 15], [13, 10, 12, 14]], [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]], 15)
#     # result = aStar([[1, 8, 2], [None, 4, 3], [7, 6, 5]], [[1, 2, 3], [4, 5, 6], [7, 8, None]], 8)