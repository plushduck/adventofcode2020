from itertools import product

ADJ_OFFSETS = set(product(range(-1,2),repeat=2))
ADJ_OFFSETS.remove((0,0))

def inc_adj(adj_count, i, j):
    for ii,jj in ADJ_OFFSETS:
        if i+ii >= 0 and i+ii < len(adj_count) and j+jj >= 0 and j+jj < len(adj_count[0]):
            adj_count[i+ii][j+jj] += 1

def print_map(input):
    for row in input:
        print(''.join(row))

def print_counts(counts):
    for row in counts:
        print(','.join([str(s) for s in row]))

def print_occupied(input):
    count = 0
    for row in input:
        for seat in row:
            if seat == '#':
                count += 1
    print(count)

# Returns True if seats flipped, False else
def step_seats(input):
    adj_count = []
    for row in input:
        adj_count.append(len(input[0])*[0])
    flipped = False
    for i,row in enumerate(input):
        for j, seat in enumerate(row):
            if input[i][j] == '#':
                inc_adj(adj_count,i,j)
    for i,row in enumerate(input):
        for j, seat in enumerate(row):
            if input[i][j] == 'L':
                if adj_count[i][j] == 0:
                    input[i][j] = '#'
                    flipped = True
            elif input[i][j] == '#' and adj_count[i][j] >= 4:
                input[i][j] = 'L'
                flipped = True
    # print_counts(adj_count)
    # print_map(input)
    return flipped

if __name__ == '__main__':
    with open('./11/input.txt') as f:
        input = f.read().splitlines()
    input = [
        [s for s in row] for row in input
    ]
    count = 1
    while(step_seats(input)):
        count += 1
    print_occupied(input)
