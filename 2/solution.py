from collections import Counter
import re


def read_test_file(filename):
    with open(filename) as f:
        return f.read().splitlines()

test_parser_a = re.compile(r'(?P<min>.*)-(?P<max>.*) (?P<char>.+): (?P<pass>.*)')
def password_valid_a(test_str):
    m = test_parser_a.match(test_str)
    c = Counter(m.group('pass'))
    valid = c[m.group('char')] >= int(m.group('min')) and c[m.group('char')] <= int(m.group('max'))
    # print(f"test = {test_str}, {valid}")
    return valid

test_parser_b = re.compile(r'(?P<pos_1>.*)-(?P<pos_2>.*) (?P<char>.+): (?P<pass>.*)')
def password_valid_b(test_str):
    m = test_parser_b.match(test_str)
    pw = m.group('pass')
    char = m.group('char')[0]
    pos_1 = int(m.group('pos_1'))-1
    pos_2 = int(m.group('pos_2'))-1
    valid = (pw[pos_1] == char) ^ (pw[pos_2] == char)
    # print(f"test = {test_str}, {valid}")
    return valid

if __name__ == '__main__':
    tests = read_test_file('2/input_1.txt')
    print(len(list(filter(password_valid_a, tests))))
    print(len(list(filter(password_valid_b, tests))))
