import puzzle as pz

PUZZLESIZE = 15

# testing goalState
goalState = pz.goalState(PUZZLESIZE)
print(goalState)
print("---------------------------------------------\n")

# testing initialState
initialState = pz.initialState(PUZZLESIZE)
print(initialState)
print("---------------------------------------------\n")

# testing blankSpot
blankSpot = pz.blankSpot(initialState)
print(blankSpot)
print("---------------------------------------------\n")

# testing actions
acts = pz.actions(initialState)
print(acts)
print("---------------------------------------------\n")

# testing result
for act in acts:
    resultPz = pz.result(initialState, act)
    print(resultPz)
    print('\n')
print("---------------------------------------------\n")

# testing h1
h1Value = pz.h1(initialState, goalState)
#h2Value = pz.h1(resultPz, goalState)
print(h1Value)
# print(h2Value)
print("---------------------------------------------\n")

# testing puzzleSolved
pzSolved = pz.puzzleSolved(initialState, goalState)
pzSolved1 = pz.puzzleSolved(goalState, goalState)
print(pzSolved)
print(pzSolved1)
print("---------------------------------------------\n")
