#  File: Spiral.py
#  Student Name:Zimo Chen
#  Student UT EID: zc5983

import sys

# Input: n
# Output:
def get_dimension(in_data):
    try:
        dimension = int(in_data.readline())
        if dimension <= 0:
            print("Dimension is negative or 0!")
            exit()
        return dimension
    except (ValueError,TypeError):
        print("Please enter an interger!")
        exit()
    

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    def move_right(x,y):
            return x, y + 1
    def move_down(x,y):
            return x + 1, y
    def move_left(x,y):
            return x, y - 1
    def move_up(x,y):
            return x - 1, y
    
    if (n % 2 == 0):
        n = n + 1
    x = n // 2
    y = n // 2

    spiral = [[0] * n for _ in range(n)]
    value = 1
    count = 1
    spiral[x][y] = value
    value = value + 1
    
    for _ in range(x + 1):
        if count != 1:
            for _ in range(count - 1):
                x, y = move_up(x,y)
                spiral[x][y] = value
                value = value + 1
        if count < n:
            for _ in range(count):
                x, y = move_right(x,y)
                spiral[x][y] = value
                value = value + 1
        elif count == n:
            for _ in range(count - 1):
                x, y = move_right(x,y)
                spiral[x][y] = value
                value = value + 1
        if count < n:
            for _ in range(count):
                x, y = move_down(x,y)
                spiral[x][y] = value
                value = value + 1
        if count < n:
            for _ in range(count):
                x, y = move_left(x,y)
                spiral[x][y] = value
                value = value + 1
        if count < n:
            count = count + 2
            x, y = move_left(x,y)
            spiral[x][y] = value
            value = value + 1
    return spiral


# Input: handle to input file
#        the number spiral
# Output: printed adjacent sums
def print_adjacent_sums(in_data, spiral):
    for line in in_data:
        try:
            value = int(line.strip())
            if any(value in row for row in spiral):
                print(sum_adjacent_numbers(spiral, value))
            else:
                print(0)
        except ValueError:
            print("Invalid data")

# Input: the number spiral
#        the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    for x in range(len(spiral)):
        for y in range(len(spiral[x])):
            if spiral[x][y] == n:
                break
        if spiral[x][y] == n:
                break
        
    total = 0
    numbers = []
    try:
        if(x >= 0 and (y + 1) >= 0):
            numbers.append(spiral[x][y + 1])
    except IndexError:
        pass
    try:
        if((x + 1) >= 0 and (y + 1) >= 0):
            numbers.append(spiral[x + 1][y + 1])
    except IndexError:
        pass
    try:
        if((x + 1) >= 0 and y >= 0):
            numbers.append(spiral[x + 1][y])
    except IndexError:
        pass
    try:
        if((x + 1) >= 0 and (y - 1) >= 0):
            numbers.append(spiral[x + 1][y - 1])
    except IndexError:
        pass
    try:
        if(x >= 0 and (y - 1) >= 0):
            numbers.append(spiral[x][y - 1])
    except IndexError:
        pass
    try:
        if((x - 1) >= 0 and (y - 1) >= 0):
            numbers.append(spiral[x - 1][y - 1])
    except IndexError:
        pass
    try:
        if((x - 1) >= 0 and y >= 0):
            numbers.append(spiral[x - 1][y])
    except IndexError:
        pass
    try:
        if((x - 1) >= 0 and (y + 1) >= 0):
            numbers.append(spiral[x - 1][y + 1])
    except IndexError:
        pass
    total = sum(numbers)
    return total
                 

# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''

def main():

    # set the input source - change to False before submitting
    debug = False
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    # process the lines of input
    size = get_dimension(in_data)

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)
    # use following line for debugging only
    # print_spiral(spiral)

    # process adjacent sums
    print_adjacent_sums(in_data, spiral)


if __name__ == "__main__":
    main()
