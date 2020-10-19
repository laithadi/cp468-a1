import puzzle as pz
from puzzle import *


def main():

    puzzle_size = int(input("What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))

    while(puzzle_size != 8 and puzzle_size != 15 and puzzle_size != 24):
        puzzle_size = int(input("What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))

    print("Table: Puzzle Size {}".format(puzzle_size))
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print("|            puzzle #            |                   num_steps                   |                   num_nodes                   |")
   
    j = 0

    while (j != 100):
        # create the initial puzzle and goal puzzle 
        originalPuzzle = pz.initialState(puzzle_size)  
        goalPuzzle = pz.goalState(puzzle_size)  
        # run the astar algo using the 3 different heurisitics 
        h1_num_steps, h1_num_nodes = pz.aStar(originalPuzzle, goalPuzzle, 'h1')
        # print('before')
        h2_num_steps, h2_num_nodes = pz.aStar(originalPuzzle, goalPuzzle, 'h2')
        # print('afters')
        h3_num_steps, h3_num_nodes = pz.aStar(originalPuzzle, goalPuzzle, 'h3')
        # if (h1_num_nodes != 0) and (h2_num_nodes != 0) and (h3_num_nodes != 0):
            # increment j to keep track of the number of puzzles being solved
        j += 1 
        # print the results 
        print("                {}                         h1 = {}, h2 = {}, h3 = {}                      h1 = {}, h2 = {}, h3 = {}           ".format(
            j, h1_num_steps, h2_num_steps, h3_num_steps, h1_num_nodes, h2_num_nodes, h3_num_nodes))
        print("----------------------------------------------------------------------------------------------------------------------------------")
    
if __name__ == "__main__":
    main()