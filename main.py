import puzzle as pz
from puzzle import goalState, h1, puzzleSolved, h2, initialState, h3, aStar
import copy

#MAX = 100


def main():
    puzzle_size = int(input(
        "What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))
    #originalPuzzle= pz()
    # check if user input is 8/15/24, ask for input again if it is not
    while(puzzle_size != 8 and puzzle_size != 15 and puzzle_size != 24):
        puzzle_size = int(input(
            "What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))

    print("You choose {}-puzzle, now it is  time to create the puzzle for you...".format(puzzle_size))

    print("Puzzle created...Show puzzle for you now...")
    # heuristic()
    j = 1
    # # execute 100 different random puzzles
    while (j != 100):

        originalPuzzle = pz.initialState(puzzle_size)
        goalPuzzle = pz.goalState(puzzle_size)

    #     # heuristic 1
        h1_num_steps, h1_num_nodes = pz.aStar(
            originalPuzzle, goalPuzzle, puzzle_size)

    #     # heursitic 2
        h2_num_steps, h2_num_nodes = pz.aStar(
            originalPuzzle, goalPuzzle, puzzle_size)

    #     # heuristic 3
        h3_num_steps, h3_num_nodes = pz.aStar(
            originalPuzzle, goalPuzzle, puzzle_size)

    #     # list where we will store all the returned values

        j += 1
    """
    j = 0
    # execute 100 different random puzzles
    while (j != 100):
        originalPuzzle = pz.initialState(puzzle_size)
        #gameOver = puzzleSolved(originalPuzzle, goalState(puzzle_size))

        # deepcopy original puzzle
        puzzle4Execute = copy.deepcopy(originalPuzzle)
        # run three different heuristic functions
        # if(not gameOver):
        h1_mt = h1(puzzle4Execute, goalState(puzzle_size))
        #gameOver = False
        # if(not gameOver):
        h2_mt = h2(puzzle4Execute, goalState(puzzle_size))
        #gameOver = False
        # if(not gameOver):
        h3_mt = h3(puzzle4Execute, goalState(puzzle_size))
        # check which heuristic function has least misplaced Tiles
        if (h1_mt < h2_mt < h3_mt):
            smallest_mt = h1_mt
        elif (h2_mt < h1_mt < h3_mt):
            smallest_mt = h2_mt
        elif (h3_mt < h1_mt < h2_mt):
            smallest_mt = h3_mt
        # use heuristic function with shortest path to do A* search
        
    aStar(puzzle4Execute, goalState, puzzle_size)

    j += 1
    """

    # # format and display the table

    print("Show Table...")
    print("------------------------------------")
    print("| puzzle # | num_steps | num_nodes |")
    for k in range(100):
        print("| {} | h1 = {}, h2 = {}, h3 = {} | h1 = {}, h2 = {}, h3 = {} |")
    print("------------------------------------")


if __name__ == "__main__":
    main()

# gameOver = puzzleSolved(originalPuzzle, goalState(puzzle_size))
# # deepcopy original puzzle
# puzzle4Execute = copy.deepcopy(originalPuzzle)
# # run three different heuristic functions
# if(not gameOver):
#     h1_mt = h1(puzzle4Execute, goalState(puzzle_size))
# #gameOver = False
# # if(not gameOver):
#     h2_mt = h2(puzzle4Execute, goalState(puzzle_size))
# #gameOver = False
# # if(not gameOver):
#     h3_mt = h3(puzzle4Execute, goalState(puzzle_size))
# # check which heuristic function has least misplaced Tiles
# if (h1_mt < h2_mt < h3_mt):
#     smallest_mt = h1_mt
# elif (h2_mt < h1_mt < h3_mt):
#     smallest_mt = h2_mt
# elif (h3_mt < h1_mt < h2_mt):
#     smallest_mt = h3_mt
# # use heuristic function with shortest path to do A* search
# aStar(puzzle4Execute, goalState, puzzle_size)
