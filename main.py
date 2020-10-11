import puzzle as pz
from puzzle import goalState, h1, puzzleSolved, h2, initialState, h3


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
    j = 0

    while (j != 100):
        originalPuzzle = puzzleCreated
        if(not gameOver):
            h1_mt = h1(originalPuzzle, goalState(puzzle_size))
        gameOver = False
        if(not gameOver):
            h2_mt = h2(originalPuzzle, goalState(puzzle_size))
        gameOver = False
        if(not gameOver):
            h3_mt = h3(originalPuzzle, goalState(puzzle_size))
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

        j += 1

        # # formate and display the table

    print("Show Table...")
    print("-------------")
    if puzzle_size == 8:
        for i in range(3):
            print("|{}|{}|{}|".format(
                puzzleCreated[i][0], puzzleCreated[i][1], puzzleCreated[i][2]))
    elif puzzle_size == 15:
        for i in range(4):
            print("|{}|{}|{}|{}|".format(
                puzzleCreated[i][0], puzzleCreated[i][1], puzzleCreated[i][2], puzzleCreated[i][3]))
    elif puzzle_size == 24:
        for i in range(4):
            print("|{}|{}|{}|{}|{}|".format(
                puzzleCreated[i][0], puzzleCreated[i][1], puzzleCreated[i][2], puzzleCreated[i][3], puzzleCreated[i][4]))


if __name__ == "__main__":
    main()
