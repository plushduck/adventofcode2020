from collections import Counter
import re


def read_test_file(filename):
    with open(filename) as f:
        return f.read().splitlines()

test_parser = re.compile(r'(?P<min>.*)-(?P<max>.*) (?P<char>.+): (?P<pass>.*)')

def password_valid(test_str):
    m = test_parser.match(test_str)
    c = Counter(m.group(4))
    valid = c[m.group('char')] >= int(m.group('min')) and c[m.group('char')] <= int(m.group('max'))
    print(f"test = {test_str}, {valid}")
    return valid

if __name__ == '__main__':
    tests = read_test_file('2/input_1.txt')
    valid_count = len(list(filter(password_valid, tests)))
    print(valid_count)

