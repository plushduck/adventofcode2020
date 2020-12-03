def read_test_file(filename):
    with open(filename) as f:
        return f.read().splitlines()


def get_trees_for_slope(test, delta_x, delta_y):
    test = read_test_file('./3/input.txt')
    pos_x = 0
    modulo = len(test[0])
    trees = 0
    for i,row in enumerate(test[delta_y:]):
        if i % delta_y != 0:
            continue
        pos_x += delta_x
        pos_x %= modulo
        if row[pos_x] == '#':
            trees += 1
    return trees



# 176
if __name__ == "__main__":

    test = read_test_file('./3/input.txt')
    # Part 1
    print(get_trees_for_slope(test, 3, 1))

    # Part 2
    '''
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    '''
    slopes = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
    ]
    product = 1
    for slope in slopes:
        product *= get_trees_for_slope(test, slope[0], slope[1])
    print(product)