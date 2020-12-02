
def VerifyPassword(policy, password):
    chars = password.count(policy.char)
    if chars < policy.range[0]:
        return False
    elif chars > policy.range[1]:
        return False
    return True

def VerifyPasswordPartTwo(policy, password):
    pos1 = password[policy.range[0]-1] == policy.char
    pos2 = password[policy.range[1]-1] == policy.char
    return pos1 != pos2

def ValidatePasswords(policies, passwords):
    valid_passwords = 0
    for i in range(len(policies)):
        if VerifyPassword(policies[i], passwords[i]):
            valid_passwords += 1
    return valid_passwords

def ValidatePasswordsPartTwo(policies, passwords):
    valid_passwords = 0
    for i in range(len(policies)):
        if VerifyPasswordPartTwo(policies[i], passwords[i]):
            valid_passwords += 1
    return valid_passwords


class Day2:
    run_tests = True
    def __init__(self, run_tests = True):
        self.run_tests = run_tests

    def run(self):
        if self.run_tests:
            print("Running tests")

            print("Running part 1 example")
            result = ValidatePasswords(
                [PasswordPolicy((1, 3), 'a'), PasswordPolicy((1, 3), 'b'), PasswordPolicy((2, 9), 'c')], 
                ["abcde", "cdefg", "ccccccccc"]
            )
            assert(result == 2)

            print("Running part 2 example")
            result = ValidatePasswordsPartTwo(
                [PasswordPolicy((1, 3), 'a'), PasswordPolicy((1, 3), 'b'), PasswordPolicy((2, 9), 'c')], 
                ["abcde", "cdefg", "ccccccccc"]
            )
            assert(result == 1)
        
        file = open('day2/input.txt', 'r') 
        
        valid_passwords_part1 = 0
        valid_passwords_part2 = 0
        while True:
            line = file.readline() 
        
            if not line:
                break
            # Just some messy string manipulation
            line = line.strip()
            val = line.split(": ")
            password = val[1]
            temp = val[0].split(" ")
            char = temp[1]
            str_range=temp[0].split("-")
            range=(int(str_range[0]), int(str_range[1]))
            
            policy = PasswordPolicy(range, char)
            if VerifyPassword(policy, password):
                valid_passwords_part1 += 1
            if VerifyPasswordPartTwo(policy, password):
                valid_passwords_part2 += 1
        print (f"Result of Part 1: {valid_passwords_part1}")
        print (f"Result of Part 2: {valid_passwords_part2}")


class PasswordPolicy:
    range = (0, 0)
    char = 'a'

    def __init__(self, range, char):
        self.range = range
        self.char = char