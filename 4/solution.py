from dataclasses import dataclass
import re


'''
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''

@dataclass
class Passport:
    byr: str # Birth Year
    iyr: str # Issue Year
    eyr: str # Expiration Year
    hgt: str # Height
    hcl: str # Hair Color
    ecl: str # Eye Color
    pid: str # Passport ID
    cid: str = "" # Country ID (optional)

    def is_valid():


field_pair_parser = re.compile(r'(?P<name>.*):(?P<value>.*)')

def passport_args_valid(kwargs):
    try:
        Passport(kwargs)
    except TypeError:
        return False
    return True

def count_valid_passports(filename):
    with open(filename) as f:

        # Split input file into per-passport sections
        full_input = f.read()
        passport_inputs = full_input.split('\n\n')

        valid_count = 0
        for passport_input in passport_inputs:
            kwarg_dict = {}
            input_pairs = (passport_input.replace('\n', ' ')).split()
            for pair in input_pairs:
                m = field_pair_parser.match(pair)
                kwarg_dict[m.group('name')] = m.group('value')
            try:
                Passport(**kwarg_dict)
                valid_count += 1
            except TypeError as e:
                pass
        return valid_count

if __name__ == "__main__":

    # Part 1:
    print(count_valid_passports('./4/input.txt'))
