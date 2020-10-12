import puzzle as pz

PUZZLESIZE = 15

# testing goalState
goalState = pz.goalState(PUZZLESIZE)
print("This is the GOALSTATE: ")
print(goalState)
print("---------------------------------------------\n")

# testing initialState
initialState = pz.initialState(PUZZLESIZE)
print("This is the INITIAL STATE")
print(initialState)
print("---------------------------------------------\n")

# testing blankSpot
blankSpot = pz.blankSpot(initialState)
print("This is the coordinates to the BLANK SPOT in the puzzle: ")
print(blankSpot)
print("---------------------------------------------\n")

# testing actions
acts = pz.actions(initialState)
print("These are the set of coordinates we can move (interchange) with the blank spot. \nthe different moves the AI can take: ")
print(acts)
print("---------------------------------------------\n")


# testing result 
for act in acts:
    print("This is the result of making a move from the list of actions we can take from above: ")
    resultPz = pz.result(initialState, act)
    print(resultPz)
    print('\n')
print("---------------------------------------------\n")

# testing h1
print("This is the heuristic value (h1): ")
h1Value = pz.h1(initialState, goalState)
#h2Value = pz.h1(resultPz, goalState)
print(h1Value)
# print(h2Value)
print("---------------------------------------------\n")

# testing puzzleSolved
print("This tells us if the puzzle is solved or not: ")
pzSolved = pz.puzzleSolved(initialState, goalState)
pzSolved1 = pz.puzzleSolved(goalState, goalState)
print(pzSolved)
print(pzSolved1)
print("---------------------------------------------\n")
