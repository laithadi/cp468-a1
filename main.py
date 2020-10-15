import puzzle as pz
from puzzle import goalState, h1, puzzleSolved, h2, initialState, h3, aStar
import copy


def main():
    puzzle_size = int(input(
        "What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))
    # check if user input is 8/15/24, ask for input again if it is not
    while(puzzle_size != 8 and puzzle_size != 15 and puzzle_size != 24):
        puzzle_size = int(input(
            "What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))
    print("You choose {}-puzzle, now it is  time to create the puzzle for you...".format(puzzle_size))
    originalPuzzle = pz.initialState(puzzle_size)
    print("Puzzle created...Show puzzle for you now...")
    # heuristic()

    gameOver = puzzleSolved(originalPuzzle, goalState(puzzle_size))
    j = 0
    # execute 100 different random puzzles
    while (j != 100):
        # deepcopy original puzzle
        puzzle4Execute = copy.deepcopy(originalPuzzle)
        # run three different heuristic functions
        if(not gameOver):
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
        aStar(puzzle4Execute, goalState(puzzle_size), puzzle_size)

        j += 1

    # # format and display the table

    print("Show Table...")
    print("-------------")
    if puzzle_size == 8:
        for i in range(3):
            print("|{}|{}|{}|".format(
                puzzle4Execute[i][0], puzzle4Execute[i][1], puzzle4Execute[i][2]))
    elif puzzle_size == 15:
        for i in range(4):
            print("|{}|{}|{}|{}|".format(
                puzzle4Execute[i][0], puzzle4Execute[i][1], puzzle4Execute[i][2], puzzle4Execute[i][3]))
    elif puzzle_size == 24:
        for i in range(4):
            print("|{}|{}|{}|{}|{}|".format(
                puzzle4Execute[i][0], puzzle4Execute[i][1], puzzle4Execute[i][2], puzzle4Execute[i][3], puzzleCreated[i][4]))


if __name__ == "__main__":
    main()
