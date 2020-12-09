seat = "FFFBBBFRRR"

def get_seat(str_rep):
    str_rep = str_rep.replace('F', '0')
    str_rep = str_rep.replace('B', '1')
    str_rep = str_rep.replace('L', '0')
    str_rep = str_rep.replace('R', '1')
    row = int(str_rep[0:7],2)
    col = int(str_rep[7:],2)
    return 8*row + col

if __name__ == "__main__":
    with open('./5/input.txt') as f:
        # Part 1
        codes = f.read().splitlines()
        seats = [get_seat(code) for code in codes]
        print(max(seats))

        # Part 2
        seats.sort()
        i = 0
        while seats[i+1] == seats[i]+1:
            i += 1
        print(seats[i]+1)
