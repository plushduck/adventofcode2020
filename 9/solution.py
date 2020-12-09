def is_valid(addends, value):
    found = set()
    for a in addends:
        if value-a in found:
            return True
        found.add(a)
    return False

def find_weakness(values, preamble_count):
    for i in range(preamble_count,len(values)):
        if not is_valid(values[i-preamble_count:i], values[i]):
            return values[i]

def encryption_weakness(values, weakness):
    lower = 0
    upper = 1
    total = values[lower] + values[upper]
    while True:
        if total == weakness:
            return min(values[lower:upper+1]) + max(values[lower:upper+1])
        if total < weakness:
            upper +=1
            total += values[upper]
        elif total > weakness:
            total -= values[lower]
            lower += 1

if __name__ == '__main__':
    with open('./9/input.txt') as f:
        values = [int(line) for line in f.read().splitlines()]

    # Part 1
    weakness = find_weakness(values, 25)
    print(weakness)

    # Part 2
    print(encryption_weakness(values, weakness))

