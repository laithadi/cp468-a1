import puzzle as pz

PUZZLESIZE = 8

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

# testing h2
print("This is the heuristic value (h2): ")
h2Value = pz.h2(initialState, goalState)
print(h2Value)
print("---------------------------------------------\n")

# testing h3
print("This is the heuristic value (h3): ")
h3Value = pz.h3(initialState, goalState)
print(h3Value)
print("---------------------------------------------\n")


print("---------------------------------------------\n")
# print(initialState)

print('A* tests')

#implementing A*
#initialState= initialState.tolist()
#pz.aStar(initialState, goalState, func='h1')
# test_initial= [[1,8,2],[None,4,3],[7,6,5]]
# test_goal= [[1,2,3],[4,5,6],[7,8,None]]

#temp = pz.aStarh2(initialState, goalState,8)

print("---------------------------------------------\n")
print("---------------------------------------------\n")
print("---------------------------------------------\n")
print("This is goal state:", goalState)
print("This is initial state: ", initialState)
#print(temp)
print("---------------------------------------------\n")
print("---------------------------------------------\n")
print("---------------------------------------------\n")

print("---------------------------------------------\n")
print('The puzzle')
# actuala= pz.aStar(initialState,goalState,PUZZLESIZE)
# print(actuala)


# # testing puzzleSolved
# print("This tells us if the puzzle is solved or not: ")
# pzSolved = pz.puzzleSolved(initialState, goalState)
# pzSolved1 = pz.puzzleSolved(goalState, goalState)

# print(pzSolved)
# print(pzSolved1)
# print("---------------------------------------------\n")
print("h1 testaz")
temp1 = pz.aStarh2(initialState, goalState, 8)

print("h1 testaz")
temp3 = pz.aStarh1(initialState, goalState, 8)

print("h3 testaz")
temp2 = pz.aStarh3(initialState, goalState, 8)
