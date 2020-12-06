import math

def get_seat_id(pass_num):
    length = len(pass_num)
    lower_bound = 0
    upper_bound = 127
    last_index = 0
    for i in range(length):
        if pass_num[i] == 'F':
            upper_bound = lower_bound + math.floor((upper_bound - lower_bound) / 2)
            #print(f"upper bound: {upper_bound}")
        elif pass_num[i] == 'B':
            lower_bound = lower_bound + math.ceil((upper_bound - lower_bound) / 2)
            #print(f"lower bound: {lower_bound}")
        elif pass_num[i] == 'R' or pass_num[i] == 'L':
            last_index = i
            break
    assert(lower_bound == upper_bound)
    row = lower_bound

    lower_bound = 0
    upper_bound = 7
    for i in range(last_index, length):
        if pass_num[i] == 'L':
            upper_bound = lower_bound + math.floor((upper_bound - lower_bound) / 2)
            #print(f"upper bound: {upper_bound}")
        elif pass_num[i] == 'R':
            lower_bound = lower_bound + math.ceil((upper_bound - lower_bound) / 2)
            #print(f"lower bound: {lower_bound}")
    assert(lower_bound == upper_bound)
    column = lower_bound
    return row * 8 + column


class Day5:
    run_tests = True
    def __init__(self, run_tests = True):
        self.run_tests = run_tests

    def run(self):
        if self.run_tests:
            print("Running tests")

            seat_id = get_seat_id("FBFBBFFRLR")
            assert(seat_id == 357)
            seat_id = get_seat_id("BFFFBBFRRR")
            assert(seat_id == 567)
            seat_id = get_seat_id("FFFBBBFRRR")
            assert(seat_id == 119)
            seat_id = get_seat_id("BBFFBBFRLL")
            assert(seat_id == 820)
        
        file = open('day5/input.txt', 'r') 
        
        max_seat_id=0
        seat_ids=[]
        while True:
            line = file.readline()
            if not line:
                break
            seat_id = get_seat_id(line)
            seat_ids.append(seat_id)
            max_seat_id = max(seat_id, max_seat_id)
        print(f"Answer for part 1: {max_seat_id}")

        seat_ids.sort()
        for i in range(1, len(seat_ids)-1):
            if seat_ids[i]+2 == seat_ids[i+1]:
                print(f"Good? {seat_ids[i]}, {seat_ids[i+1]}")
