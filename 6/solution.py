from collections import Counter

if __name__ == '__main__':
    with open('./6/input.txt') as f:
        input = f.read()
        groups = input.split('\n\n')

        # Part 1
        count_1 = 0
        count_2 = 0
        for group in groups:
            s = set()
            c = Counter()
            individuals = group.split('\n')
            for affirmatives in individuals:
                s = s | set(affirmatives)
                c += Counter(affirmatives)
            for k,v in c.items():
                if v == len(individuals):
                    count_2 += 1
            count_1 += len(s)
        print(count_1)
        print(count_2)