def evaluate_program(lines):

    cur_line = 0
    acc = 0

    while True:

        parsed = lines[cur_line].split(" ")
        code = parsed[0]
        value = int(parsed[1])
        lines[cur_line] = "x 1"
        if code == "nop":
            cur_line += 1
        if code == "acc":
            acc += value
            cur_line += 1
        if code == "jmp":
            cur_line += value
        if code == "x":
            acc = -1
            break
    return acc



class Day8:
    run_tests = True
    def __init__(self, run_tests = True):
        self.run_tests = run_tests

    def run(self):
        if self.run_tests:
            print("Running tests")
            test_input="""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
            result = evaluate_program(test_input.split("\n"))
            assert(result == 5)
        
        file_input = open("day8/input.txt", "r").read()
        lines = file_input.split("\n")
        result = evaluate_program(lines)
        print(f"Result for part 1: {result}")
        