#!/usr/bin/python3
import sys
from timeit import timeit
from day1.day1 import Day1

days_completed=2

def get_day(day_num):
    if day_num == -1:
        print("Running all tests")
    elif day_num == 1:
        return Day1().run
    elif day_num == 2:
        return Day1().run
    else:
        raise BaseException()

def run_all_tasks():
    for i in range(days_completed):
        print(f'!~-- Running day {i+1} --~!')
        get_day(i+1)()

print("Welcome to hcorion's Advent of Code 2020")

print("Which challenge would you like to participate in?")
print("Type the number of the day that you want to run. Type 'a' to run all the days.")

has_valid_input = False
task_to_run=0
day_to_run=0

command_line_input=None
if len(sys.argv) > 0:
    print("Attempting to read from command line params!")
    command_line_input=sys.argv[1]

while not has_valid_input:
    if command_line_input != None:
        val = command_line_input
    else:
        val = input("Enter your value: ")

    if val.lower() == 'a':
        task_to_run=run_all_tasks
        day_to_run = -1
        has_valid_input = True
        break
    try: 
        day_num = int(val)
        task_to_run=get_day(day_num)
        day_to_run = day_num
        has_valid_input = True
    except ValueError:
        print(f"Invalid input: {val}, not a number, or the letter 'a'!")
    except BaseException:
        print(f"Invalid input: {val}! That day does not exist!")
    
    if command_line_input != None:
        command_line_input = None

print("==-=-== Running all days! ==-=-==\n" if day_to_run == -1 else f"!~-- Running day {day_to_run}! --~!")
time_to_run = timeit(lambda: task_to_run(), number = 1)
print(f"\n All tasks took {time_to_run} seconds to complete!")