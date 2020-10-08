def main():
    puzzle_size = int(input(
        "What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))
    while(puzzle_size != 8 and puzzle_size != 15 and puzzle_size != 24):
        puzzle_size = int(input(
            "What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))
    print("You choose {}-puzzle, now it is  time to create the puzzle for you...".format(puzzle_size))
    # create_puzzle(puzzle_size)
    print("Puzzle created...Show puzzle for you now...")
    # a_star_search()
    # heuristic()


if __name__ == "__main__":
    main()
