def initialState():
    """
    Returns the initial state of the puzzle 
    """
    pass


def actions(puzzle):
    """
    Returns set of all possible actions available on the puzzle 
    """
    pass


def puzzleSolved(puzzle):
    """ 
    Returns whether the puzzle is solved or not 
    """
    pass


def h1(currentState, goalState):
    """
    Takes current state and goal state of puzzle. Then calculates the number of misplaced tiles. 
    ---------------------------------------------------------------------------------------------
    Parameteres:
        currentState: current state of the puzzle 
        goalState: goal state of the puzzle we are trying to achieve 
    """

    length = len(currentState)

    for i in range(0, length):
        for j in range(0, length):
            if (currentState[i][j] != goalState[i][j]):
                misplacedTiles += 1 

    return misplacedTiles 