from pyparsing import *

def get_valid_passports(input_str):
    valid_passports = 0
    lines = input_str.split("\n\n")
    for line in lines:
        line = line.replace("\n", " ")
        sections = line.split(" ")
        result = 0
        for section in sections:
            if not section.isspace() and section != '':
                val =  compare_section(section)
                if val == 0:
                    print (f"bad result: \"{section}\"")
                result |= val
        
        if result ^ 0b11111111 == 0 or result ^ 0b1111111 == 0:
            valid_passports += 1
        
    return valid_passports

def compare_section(section):
    label = section.split(":")[0].lower()
    data = section.split(":")[1].lower()
    if label == "byr":
        year = int(data)
        if year >= 1920 and year <= 2002:
            return 0b1
    elif label == "iyr":
        year = int(data)
        if year >= 2010 and year <= 2020:
            return 0b10
    elif label == "eyr":
        year = int(data)
        if year >= 2020 and year <= 2030:
            return 0b100
    elif label == "hgt":
        if data.endswith("cm"):
            height = float(data.rstrip("cm"))
            if height >= 150 and height <= 193:
                return 0b1000
        elif data.endswith("in"):
            height = float(data.rstrip("in"))
            if height >= 59 and height <= 76:
                return 0b1000
    elif label == "hcl":
        if re.match("^#(?:[0-9a-fA-F]{3}){1,2}$", data):
            return 0b10000
    elif label == "ecl":
        if re.match("(amb|blu|brn|gry|grn|hzl|oth)", data):
            return 0b100000
    elif label == "pid":
        if re.match("\d{9}$", data):
            return 0b1000000
    elif label == "cid":
        return 0b10000000
    else:
        raise BaseException()
    return 0



class Day4:
    run_tests = True
    def __init__(self, run_tests = True):
        self.run_tests = run_tests

    def run(self):
        if self.run_tests:
            self.tests()

        file_input = open("day4/input.txt", "r").read()
        result = get_valid_passports(file_input)
        print (f"Result of part 1: {result}")
    
    def tests(self):
        print("Running tests")

        input_str = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
        result = get_valid_passports(input_str)
        assert(result == 2)

        print ("Running part two tests")

        input_str="""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
        result = get_valid_passports(input_str)
        assert(result == 4)
        