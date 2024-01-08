#  File: Josephus.py
#  Student Name: Zimo Chen
#  Student UT EID: zc5983

import sys


# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data):
        new_soldier = Link(data)
        if self.first == None:
            self.first = new_soldier
            self.last = new_soldier
        else:
            self.last.next = new_soldier
            new_soldier.next = self.first
            self.last = new_soldier

    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current_node = self.first
        if not current_node:
            return None 
        while True:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
            if current_node == self.first:
                break  
        return None 

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):
        current_node = self.first
        previous_node = None

        if (self.find(data) != None):
            while current_node:
                if current_node.data == data:
                    if previous_node:
                        previous_node.next = current_node.next
                    else:
                        self.first = current_node.next
                    return current_node
                else:
                    previous_node = current_node
                    current_node = current_node.next
            return None

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order

    def delete_after(self, start, step):
        current_node = self.first # start
        previous_node = None
        count = 0

        while current_node and count < step:
            previous_node = current_node
            current_node = current_node.next
            count += 1

        if current_node:
            deleted_data = current_node.data
            previous_node.next = current_node.next
            return deleted_data, current_node.next

        return None, None

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        result = []
        current_node = self.first

        if not current_node:
            return "[]"

        while True:
            result.append(str(current_node.data))
            current_node = current_node.next
            if current_node == self.first:
                break

        return "[" + ", ".join(result) + "]"


# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):
    if num_soldiers < 1:
        return None
    
    num_list = CircularList()
    for i in range(1, num_soldiers + 1):
        num_list.insert(i)

    return num_list

# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    if (my_list == None) or (num_soldiers < 1) or (step_count < 1):
        return

    current_node = my_list.first

    while current_node.data != start_data:
        current_node = current_node.next

    while num_soldiers > 0:
        deleted_data, next_node = my_list.delete_after(current_node, step_count)
        print(deleted_data, end=' ')
        num_soldiers -= 1

        if num_soldiers > 0:
            print()
            current_node = next_node


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    for i in range(1, 6):
        my_list.insert(i)

    # Step 2: Print the list using __str__
    print("Original List:", my_list.__str__())

    # Step 3: Delete 4 from the list
    deleted_node = my_list.delete(6)
    if deleted_node:
        print(f"Deleted Node: {deleted_node.data}")
    else:
        print("Node not found!")

    # Step 4: Print the new list
    print("Updated List:", my_list.__str__())


    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()
