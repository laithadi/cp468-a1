import puzzle as pz
from puzzle import initialState
from puzzle import goalState, h1, puzzleSolved, h2


def main():
    puzzle_size = int(input(
        "What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))
    while(puzzle_size != 8 and puzzle_size != 15 and puzzle_size != 24):
        puzzle_size = int(input(
            "What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))
    print("You choose {}-puzzle, now it is  time to create the puzzle for you...".format(puzzle_size))
    puzzleCreated = pz.initialState(puzzle_size)
    print("Puzzle created...Show puzzle for you now...")
    # heuristic()

    gameOver = puzzleSolved(puzzleCreated, goalState(puzzle_size))
    i = 0

    while (i != 100):
        originalPuzzle = puzzleCreated
        if(not gameOver):
            h1(originalPuzzle, goalState(puzzle_size))
        if(not gameOver):
            h2(originalPuzzle, goalState(puzzle_size))
        if(not gameOver):
            h3(originalPuzzle, goalState(puzzle_size))
            #     # create a OGpuzzle
            #     OGpuzzle = pz.initialState(puzzle_size)

            #     # solve the puzzle
            #     while (not gameOver):
            #         # deepcopy the OGpuzzle

            #         # heuristic 1

            #     while (not gameOver):
            #         # deepcopy the OGpuzzle

            #         # heuristic 2

            #     while (not gameOver):
            #         # deepcopy the OGpuzzle

            #         # heuristic 2

            #     i += 1

            # # formate and display the table


if __name__ == "__main__":
    main()
