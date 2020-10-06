empty = None

def createInitialPuzzle(size):
    
    # if size of puzzle is 8
    if size == 8: 
        initialPuzzle = [
        [empty, empty, empty],
        [empty, empty, empty],
        [empty, empty, empty]
        ]

    # if size of puzzle is 15 
    elif size == 15:
        initialPuzzle = [
        [empty, empty, empty, empty],
        [empty, empty, empty, empty],
        [empty, empty, empty, empty],
        [empty, empty, empty, empty]
        ]

    # if size of puzzle is 24 
    else:
        initialPuzzle = [
        [empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty]
        ]

    return initialPuzzle

# def check_solvability(state):
#         """ Checks if the given state is solvable """

#         inversion = 0
#         for i in range(len(state)):
#             for j in range(i + 1, len(state)):
#                 if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
#                     inversion += 1

#         return inversion % 2 == 0

def goalTest(currentState, goalState):
    pass
    





p = createInitialPuzzle(8) 

p[0][0] = 1
p[0][1] = 6
p[0][2] = 5
p[1][0] = 7
p[1][2] = 2
p[2][0] = 8
p[2][1] = 3
p[2][2] = 4

print(p)
