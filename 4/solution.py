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


field_pair_parser = re.compile(r'(?P<name>.*):(?P<value>.*)')

'''
Field rules

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''
FIELD_PARSERS = {
    'byr': re.compile(r'\d{4}'),
    'iyr': re.compile(r'\d{4}'),
    'eyr': re.compile(r'\d{4}'),
    'hgt': re.compile(r'(\d{3}cm|\d{2}in)'),
    'hcl': re.compile(r'#[0-9a-f]{6}'),
    'ecl': re.compile(r'(amb|blu|brn|gry|grn|hzl|oth)'),
    'pid': re.compile(r'\d{9}')
}

def year_field_valid(kwargs, name, min_year, max_year):
    year = int(kwargs[name])
    return year >= min_year and year <= max_year

def passport_args_valid(kwargs):
    for k,v in kwargs.items():
        if k in FIELD_PARSERS:
            if not FIELD_PARSERS[k].fullmatch(v):
                return False

    if not year_field_valid(kwargs, 'byr', 1920, 2002):
        return False
    if not year_field_valid(kwargs, 'iyr', 2010, 2020):
        return False
    if not year_field_valid(kwargs, 'eyr', 2020, 2030):
        return False
    if kwargs['hgt'][-2:] == 'cm':
        hgt = int(kwargs['hgt'][:3])
        if hgt < 150 or hgt > 193:
            return False
    else:
        hgt = int(kwargs['hgt'][:2])
        if hgt < 59 or hgt > 76:
            return False
    return True

def count_valid_passports(filename):
    with open(filename) as f:

        # Split input file into per-passport sections
        full_input = f.read()
        passport_inputs = full_input.split('\n\n')

        part_1_count = 0
        part_2_count = 0
        for passport_input in passport_inputs:
            kwarg_dict = {}
            input_pairs = (passport_input.replace('\n', ' ')).split()
            for pair in input_pairs:
                m = field_pair_parser.match(pair)
                kwarg_dict[m.group('name')] = m.group('value')
            try:
                Passport(**kwarg_dict)
                part_1_count += 1
                if passport_args_valid(kwarg_dict):
                    part_2_count += 1
            except TypeError as e:
                pass
        print(part_1_count)
        print(part_2_count)

if __name__ == "__main__":

    count_valid_passports('./4/input.txt')
