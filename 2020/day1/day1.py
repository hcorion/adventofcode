import time

def find_two_ideal_values(expenses):
        start_time = time.time()
        for x in expenses:
            for y in expenses:
                if int(x) + int(y) == 2020:
                    end_time = time.time()
                    print(f"Took: {end_time - start_time} seconds")
                    return int(x) * int(y)

def find_three_ideal_values(expenses):
        required_val = 2020
        start_time = time.time()
        for x in expenses:
            x = int(x)
            for y in expenses:
                y = int(y)
                temp = x+y
                if temp >= required_val:
                    continue
                for z in expenses:
                    z = int(z)
                    if temp + z == required_val:
                        end_time = time.time()
                        print(f"Took: {end_time - start_time} seconds")
                        return x * y * z

class Day1:
    run_tests = True
    def __init__(self, run_tests = True):
        self.run_tests = run_tests    

    def run(self):
        if self.run_tests:
            print("Running tests")

            print("Running [1721, 979, 366, 299, 675, 1456]")
            val = find_two_ideal_values([1721, 979, 366, 299, 675, 1456])
            assert(val == 514579)
            print("Running [1721, 979, 366, 299, 675, 1456] Part two")
            val = find_three_ideal_values([1721, 979, 366, 299, 675, 1456])
            assert(val == 241861950)

            # Do things
        file_input = open("day1/input.txt", "r").read().split("\n")
        print("Running Part 1")

        print("Running input.txt")
        print(f"Result: {find_two_ideal_values(file_input)}")

        print("Running Part 2")
        print(f"Result: {find_three_ideal_values(file_input)}")