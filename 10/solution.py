from collections import defaultdict
import time

# Assumes values sorted
def brute_force_count_paths(values):
    if len(values) <= 2:
        return 1
    total = 0
    i = 1
    while(i < len(values) and values[i] <= values[0]+3):
        total += brute_force_count_paths(values[i:])
        i+=1
    return total

if __name__ == '__main__':
    with open('./10/input.txt') as f:
        values = f.read().splitlines()
        values = [int(i) for i in values]
        values.append(0)
        values.append(max(values)+3)
        values.sort()

    # Part 1
    delta_counts = defaultdict(int)
    for i in range(1,len(values)):
        delta_counts[values[i]-values[i-1]] += 1
    print(delta_counts[1] * delta_counts[3])

    # Part 2
    start = time.time()
    brute_start = 0
    paths = 1
    for i in range(1,len(values)):
        delta = values[i]-values[i-1]
        if delta == 3 and i != brute_start:
            paths *= brute_force_count_paths(values[brute_start:i])
            brute_start = i
    print(paths)
    print("--- %s seconds ---" % (time.time() - start))
