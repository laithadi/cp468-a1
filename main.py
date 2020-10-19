import puzzle as pz
from puzzle import *


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
    print("Show Table...")
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print("|            puzzle #            |                   num_steps                   |                   num_nodes                   |")
    # heuristic()
    j = 0
    # # execute 100 different random puzzles 47
    while (j != 100):

        originalPuzzle = pz.initialState(puzzle_size)
        goalPuzzle = pz.goalState(puzzle_size)

    #     # heuristic 1
        h1_num_steps, h1_num_nodes = pz.aStarh1(
            originalPuzzle, goalPuzzle, puzzle_size)

    #     # heursitic 2
        h2_num_steps, h2_num_nodes = pz.aStarh2(
            originalPuzzle, goalPuzzle, puzzle_size)

    #     # heuristic 3
        h3_num_steps, h3_num_nodes = pz.aStarh3(
            originalPuzzle, goalPuzzle, puzzle_size)

        j += 1

        print("                {}                         h1 = {}, h2 = {}, h3 = {}                      h1 = {}, h2 = {}, h3 = {}           ".format(
            j, h1_num_steps, h2_num_steps, h3_num_steps, h1_num_nodes, h2_num_nodes, h3_num_nodes))
        print("----------------------------------------------------------------------------------------------------------------------------------")

        
        


if __name__ == "__main__":
    main()