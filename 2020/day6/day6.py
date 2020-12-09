def get_sum_of_answers_part1(answers):
    groups = answers.split("\n\n")
    sum = 0
    for group in groups:
        char_set = set()
        group = group.replace("\n", "")
        for char in group:
            char_set.add(char)
        sum += len(char_set)
    return sum

def get_sum_of_answers_part2(answers):
    groups = answers.split("\n\n")
    sum = 0
    for group in groups:
        people = group.split("\n")
        char_sets = []
        print("start")
        for person in people:
            char_set = set()
            for char in person:
                char_set.add(char)
            char_sets.append(char_set)
        final_char_set = char_sets[0]
        for i in char_sets:
            final_char_set = final_char_set & i
        sum += len(final_char_set)
    return sum

class Day6:
    run_tests = True
    def __init__(self, run_tests = True):
        self.run_tests = run_tests

    def run(self):
        if self.run_tests:
            print("Running tests")
            test_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""
            result = get_sum_of_answers_part1(test_input)
            assert(result == 11)
            
            result = get_sum_of_answers_part2(test_input)
            assert(result == 6)
        
        file_input = open("day6/input.txt", "r").read()
        result = get_sum_of_answers_part1(file_input)
        print(f"Part 1 output: {result}")
        file_input = open("day6/input.txt", "r").read()
        result = get_sum_of_answers_part2(file_input)
        # 1012 is too low
        # 3461 is also too low
        print(f"Part 2 output: {result}")