import puzzle as pz
from puzzle import initialState, goalState, aStar


def main():
    # ask for size of puzzle 
    puzzle_size = int(input("What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))
    # ask again if the size inputed is not an 8,15,24 
    while(puzzle_size != 8 and puzzle_size != 15 and puzzle_size != 24):
        puzzle_size = int(input("What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))
    # start printing the table 
    print("Table: Puzzle Size {}".format(puzzle_size))
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print("|            puzzle #            |                   num_steps                   |                   num_nodes                   |")
    # j is for the number of puzzles we are generating and solving 
    j = 0
    # loop for creating and solving a different puzzle each time, 100 times 
    while (j != 100):
        # create the initial puzzle and goal puzzle 
        originalPuzzle = pz.initialState(puzzle_size)  
        goalPuzzle = pz.goalState(puzzle_size)  
        # check if puzzle is solvable 
        if pz.is_puzzle_solvable(originalPuzzle) == True: 
            print("TRUE")
            print(originalPuzzle)
            # run the astar algo using the 3 different heurisitics 
            h1_num_steps, h1_num_nodes = pz.aStar(originalPuzzle, goalPuzzle, 'h1')
            h2_num_steps, h2_num_nodes = pz.aStar(originalPuzzle, goalPuzzle, 'h2')
            h3_num_steps, h3_num_nodes = pz.aStar(originalPuzzle, goalPuzzle, 'h3')
            # increment the number of puzzles solved 
            j += 1 
            # print the results 
            print("                {}                         h1 = {}, h2 = {}, h3 = {}                      h1 = {}, h2 = {}, h3 = {}           ".format(
                j, h1_num_steps, h2_num_steps, h3_num_steps, h1_num_nodes, h2_num_nodes, h3_num_nodes))
            print("----------------------------------------------------------------------------------------------------------------------------------")

        else:
            print("FALSE")

if __name__ == "__main__":
    main()