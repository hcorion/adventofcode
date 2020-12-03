def calculate_path(grid, x_depth=3, y_depth=1):
    width = len(grid.split("\n")[0])
    grid = grid.replace("\n", "")
    height = len(grid) / width
    
    trees_hit=0
    y_pos = 0
    x_pos = 0
    while y_pos < height-1:
        y_pos += y_depth
        x_pos = (x_pos + x_depth) % width
        index = hash_location(x_pos, y_pos, width)
        if grid[index] == '#':
            trees_hit += 1
    return trees_hit

def hash_location(x_pos, y_pos, width):
    return x_pos + width * y_pos

class Day3:
    run_tests = True
    def __init__(self, run_tests = True):
        self.run_tests = run_tests

    def run(self):
        if self.run_tests:
            print("Running tests")

            test_input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
            result = calculate_path(test_input)
            assert(result == 7)

        print("Running part 1")
        file_input = open("day3/input.txt", "r").read()
        result = calculate_path(file_input)
        assert(result == 167)
        print(f"Result: {result}")

        print("Running part 2")
        result = (calculate_path(file_input, 1, 1) * calculate_path(file_input, 3, 1) *
            calculate_path(file_input, 5, 1) * calculate_path(file_input, 7, 1) * calculate_path(file_input, 1, 2))
        print(f"Result: {result}")
