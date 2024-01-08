#  File: Work.py
#  Student Name: Zimo Chen
#  Student UT EID: zc5983

import sys
import time


# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep. Must be implemented
#          using recursion.
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep
def sum_series(lines_before_coffee, prod_loss):
    if lines_before_coffee <= 0:
        return 0
    else:
        current_term = lines_before_coffee // prod_loss
        return lines_before_coffee  + sum_series(current_term, prod_loss)


# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def linear_search(total_lines, prod_loss):
    if (total_lines > 2):
        for i in range(2, total_lines + 1):
            # time.sleep(0.001)
            if sum_series(i, prod_loss) >= total_lines:
                return i, i
    else:
        return total_lines, 1
    return i, i


# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def binary_search (total_lines, prod_loss):
    high = total_lines
    low = 0
    count = 0
    while high > low:
        mid = (high + low) // 2 
        m_val = sum_series(mid, prod_loss)
        # time.sleep(0.001)
        count += 1
        if m_val == total_lines:
            break
        elif m_val < total_lines:
            low = mid + 1 
        elif m_val > total_lines:
            high = mid - 1
    
    if (0 <= sum_series(low, prod_loss) - total_lines < m_val - total_lines):
        mid = low 
    if (0 <= sum_series(high, prod_loss) - total_lines < m_val - total_lines or m_val < total_lines):
        mid = high 
    return mid, count


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Open input source
    # Change debug to false before submitting
    debug = True
    if debug:
        in_data = open('work.in')
    else:
        in_data = sys.stdin

    # read number of cases
    line = in_data.readline().strip()
    num_cases = int(line)

    for i in range(num_cases):

        # read one line for one case
        line = in_data.readline().strip()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(binary_time),
              "seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(linear_time),
              "seconds")
        print()

        # Comparison
        print("Binary Search was",
              "{0:.1f}".format(linear_time / binary_time),
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()
