from copy import deepcopy
from itertools import product

ADJ_OFFSETS = set(product(range(-1,2),repeat=2))
ADJ_OFFSETS.remove((0,0))

def inc_adj(adj_count, i, j):
    for ii,jj in ADJ_OFFSETS:
        if i+ii >= 0 and i+ii < len(adj_count) and j+jj >= 0 and j+jj < len(adj_count[0]):
            adj_count[i+ii][j+jj] += 1

def inc_los(input, adj_count, i, j, i_offset, j_offset):
    cur_i = i
    cur_j = j
    while True:
        cur_i += i_offset
        cur_j += j_offset
        if cur_i < 0 or cur_i >= len(adj_count):
            return
        if cur_j < 0 or cur_j >= len(adj_count[0]):
            return
        if input[cur_i][cur_j] == '#':
            adj_count[i][j] += 1
            return
        if input[cur_i][cur_j] == 'L':
            return

def inc_adj_los(input, adj_count, i, j):
    for i_offset, j_offset in ADJ_OFFSETS:
        inc_los(input, adj_count, i, j, i_offset, j_offset)

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
    return flipped


# Traverse a ray starting at i,j with slope (i_offset, j_offset)
# Track occupancy of the last seat passed along the way and update the 
# visibility count of visited seats accordingly.
def inc_vis_ray(input, vis_count, i, j, i_offset, j_offset):
    cur_i = i
    cur_j = j
    last_seat_occupied = False
    while True:
        if input[cur_i][cur_j] == '#':
            last_seat_occupied = True
        if input[cur_i][cur_j] == 'L':
            last_seat_occupied = False
        cur_i += i_offset
        cur_j += j_offset
        if cur_i < 0 or cur_i >= len(vis_count):
            return
        if cur_j < 0 or cur_j >= len(vis_count[0]):
            return
        if last_seat_occupied:
            vis_count[cur_i][cur_j] += 1

# Get the count of perceived visible seats from each position in the input map
def get_vis_count(input):
    vis_count = []
    for row in input:
        vis_count.append(len(input[0])*[0])
    nrows = len(input)
    ncols = len(input[0])
    for i in range(nrows):
        inc_vis_ray(input, vis_count, i, 0, 0, 1)
        inc_vis_ray(input, vis_count, i, ncols-1, 0, -1)
        inc_vis_ray(input, vis_count, i, 0, 1, 1)
        inc_vis_ray(input, vis_count, i, ncols-1, 1, -1)
        inc_vis_ray(input, vis_count, i, 0, -1, 1)
        inc_vis_ray(input, vis_count, i, ncols-1, -1, -1)
    for j in range(ncols):
        inc_vis_ray(input, vis_count, 0, j, 1, 0)
        inc_vis_ray(input, vis_count, nrows-1, j, -1, 0)
        if j != 0:
            inc_vis_ray(input, vis_count, 0, j, 1, 1)
            inc_vis_ray(input, vis_count, nrows-1, j, -1, 1)
        if j != ncols-1:
            inc_vis_ray(input, vis_count, 0, j, 1, -1)
            inc_vis_ray(input, vis_count, nrows-1, j, -1, -1)
    return vis_count


# Returns True if seats flipped, False else
def step_seats_los(input):

    adj_count = get_vis_count(input)
    # print_map(input)
    # print_counts(adj_count)
    # print("")
    flipped = False
    for i,row in enumerate(input):
        for j, seat in enumerate(row):
            if input[i][j] == 'L':
                if adj_count[i][j] == 0:
                    input[i][j] = '#'
                    flipped = True
            elif input[i][j] == '#' and adj_count[i][j] >= 5:
                input[i][j] = 'L'
                flipped = True
    return flipped


if __name__ == '__main__':
    with open('./11/input.txt') as f:
        input = f.read().splitlines()
    input = [
        [s for s in row] for row in input
    ]
    input2 = deepcopy(input)

    # Part 1
    while(step_seats(input)):
        pass
    print_occupied(input)

    # Part 2
    while(step_seats_los(input2)):
         pass
    print_occupied(input2)
