#  File: BST_AVLTree.py
#  Student Name: Zimo Chen
#  Student UT EID: zc5983
#  UPDATED Monday July 27 3:15pm - Updates commented with "line update" comments


import sys


# Node class for the tree.
class Node:
    # Constructor with a key parameter creates the Node object.
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.lChild = None
        self.rChild = None
        self.height = 0

    # Calculate the current nodes' balance factor,
    # defined as height(left subtree) - height(right subtree)
    def get_balance(self):
        # Get current height of left subtree, or -1 if None
        left_height = -1
        if self.lChild is not None:
            left_height = self.lChild.height

        # Get current height of right subtree, or -1 if None
        right_height = -1
        if self.rChild is not None:
            right_height = self.rChild.height

        # Calculate the balance factor.
        return left_height - right_height

    # Recalculate the current height of the subtree rooted at
    # the node, usually called after a subtree has been
    # modified.
    def update_height(self):
        # Get current height of left subtree, or -1 if None
        left_height = -1
        if self.lChild is not None:
            left_height = self.lChild.height

        # Get current height of right subtree, or -1 if None
        right_height = -1
        if self.rChild is not None:
            right_height = self.rChild.height

        # Assign self.height with calculated node height.
        self.height = max(left_height, right_height) + 1

    # Assign either the left or right data member with a new
    # child. The parameter which_child is expected to be the
    # string "left" or the string "right". Returns True if
    # the new child is successfully assigned to this node, False
    # otherwise.
    def set_child(self, which_child, child):
        # Ensure which_child is properly assigned.
        if which_child != "left" and which_child != "right":
            return False

        # Assign the left or right data member.
        if which_child == "left":
            self.lChild = child
        else:
            self.rChild = child

        # Assign the parent data member of the new child,
        # if the child is not None.
        if child is not None:
            child.parent = self

        # Update the node's height, since the subtree's structure
        # may have changed.
        self.update_height()
        return True

    # Replace a current child with a new child. Determines if
    # the current child is on the left or right, and calls
    # set_child() with the new node appropriately.
    # Returns True if the new child is assigned, False otherwise.
    def replace_child(self, current_child, new_child):
        if self.lChild is current_child:
            return self.set_child("left", new_child)
        elif self.rChild is current_child:
            return self.set_child("right", new_child)

        # If neither of the above cases applied, then the new child
        # could not be attached to this node.
        return False


# The Tree!
class Tree:
    # Constructor to create an empty AVLTree. There is only
    # one data member, the tree's root Node, and it starts
    # out as None.
    def __init__(self, avl=False):
        self.root = None
        self.is_AVL = avl

    # Populates a tree with data from a list.
    def fill_tree(self, data):
        for d in data:
            self.insert(d)

    # Performs a left rotation at the given node. Returns the
    # new root of the subtree.
    def rotate_left(self, node):
        # Define a convenience pointer to the left child of the
        # right child.
        right_left_child = node.rChild.lChild

        # Step 1 - the right child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached
        # later.
        if node.parent is not None:
            node.parent.replace_child(node, node.rChild)
        else:  # node is root
            self.root = node.rChild
            self.root.parent = None

        # Step 2 - the node becomes the left child of what used
        # to be its right child, but is now its parent. This will
        # detach right_left_child from the tree.
        node.rChild.set_child('left', node)

        # Step 3 - reattach right_left_child as the right child of node.
        node.set_child('right', right_left_child)

        return node.parent

    # Performs a right rotation at the given node. Returns the
    # subtree's new root.
    def rotate_right(self, node):
        # Define a convenience pointer to the right child of the
        # left child.
        left_right_child = node.lChild.rChild

        # Step 1 - the left child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached
        # later.
        if node.parent is not None:
            node.parent.replace_child(node, node.lChild)
        else:  # node is root
            self.root = node.lChild
            self.root.parent = None

        # Step 2 - the node becomes the right child of what used
        # to be its left child, but is now its parent. This will
        # detach left_right_child from the tree.
        node.lChild.set_child('right', node)

        # Step 3 - reattach left_right_child as the left child of node.
        node.set_child('left', left_right_child)

        return node.parent

    # Updates the given node's height and rebalances the subtree if
    # the balancing factor is now -2 or +2. Rebalancing is done by
    # performing a rotation. Returns the subtree's new root if
    # a rotation occurred, or the node if no rebalancing was required.
    def rebalance(self, node):

        # First update the height of this node.
        node.update_height()

        # Check for an imbalance.
        if node.get_balance() == -2:

            # The subtree is too big to the right.
            if node.rChild.get_balance() == 1:
                # Double rotation case. First do a right rotation
                # on the right child.
                self.rotate_right(node.rChild)

            # A left rotation will now make the subtree balanced.
            return self.rotate_left(node)

        elif node.get_balance() == 2:

            # The subtree is too big to the left
            if node.lChild.get_balance() == -1:
                # Double rotation case. First do a left rotation
                # on the left child.
                self.rotate_left(node.lChild)

            # A right rotation will now make the subtree balanced.
            return self.rotate_right(node)

        # No imbalance, so just return the original node.
        return node

    ########### ADD CODE HERE - You won't add code RIGHT HERE, but you will need to add code somewhere in the insert() method.
    def insert(self, data):
        node = Node(data)

        # Special case: if the tree is empty, just set the root to
        # the new node.
        if self.root is None:
            self.root = node
            node.parent = None
        else:
            # Step 1 - do a regular binary search tree insert.
            current_node = self.root
            while current_node is not None:
                # Choose to go left or right
                if node.key < current_node.key:
                    # Go left. If left child is None, insert the new
                    # node here.
                    if current_node.lChild is None:
                        current_node.lChild = node
                        node.parent = current_node
                        current_node = None
                    else:
                        # Go left and do the loop again.
                        current_node = current_node.lChild
                else:
                    # Go right. If the right child is None, insert the
                    # new node here.
                    if current_node.rChild is None:
                        current_node.rChild = node
                        node.parent = current_node
                        current_node = None
                    else:
                        # Go right and do the loop again.
                        current_node = current_node.rChild

            # Step 2 - Rebalance along a path from the new node's parent up
            # to the root.
            if self.is_AVL:  # Only rebalance if the tree is AVL
                node = node.parent
                while node is not None:
                    self.rebalance(node)
                    node = node.parent

    # Get height of a tree
    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return -1
        return node.height

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the max value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0.
    # If the tree is empty the range is undefined.
    def range(self):
        def find_min_max(node):
            if node is None:
                return float('inf'), float('-inf')
            left_min, left_max = find_min_max(node.lChild)
            right_min, right_max = find_min_max(node.rChild)
            return min(node.key, left_min, right_min), max(node.key, left_max, right_max)

        min_val, max_val = find_min_max(self.root)
        if min_val == float('inf') or max_val == float('-inf'):
            return None  # Undefined for an empty tree
        return max_val - min_val


    def level(self, target_level, node=None, curr_level=0):
        if node is None:
            node = self.root
        if node is None:
            return []
        if curr_level == target_level:
            return [node]
        if node.lChild is None and node.rChild is None:
            return []
        
        nodes_at_level = []
        if node.lChild is not None:
            nodes_at_level.extend(self.level(target_level, node.lChild, curr_level + 1))
        if node.rChild is not None:
            nodes_at_level.extend(self.level(target_level, node.rChild, curr_level + 1))

        return nodes_at_level



    # Print list of nodes
    def get_node_list_str(self, nodes):
        if len(nodes) == 0:  # line update 7/17
            return "[]"      # line update 7/17
        results = "[" + str(nodes[0].key)
        for i in range(1, len(nodes)):
            results += " " + str(nodes[i].key)
        results += "]"
        return results

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        result = []
        def left_view(node, level=0):
            if node is None:
                return
            if level == len(result):
                result.append(node)
            left_view(node.lChild, level+1)
            left_view(node.rChild, level+1)

        left_view(self.root)
        return result

    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        if node.lChild is None and node.rChild is None:
            return node.key
        left_sum = self.sum_leaf_nodes(node.lChild) if node.lChild else 0
        right_sum = self.sum_leaf_nodes(node.rChild) if node.rChild else 0
        return left_sum + right_sum

    def print(self):
        self.print_helper(self.root)

    def print_helper(self, current, level=0):
        if current.rChild is not None:
            self.print_helper(current.rChild, level + 1)

        print(' ' * 3 * level + '->', current.key)

        if current.lChild is not None:
            self.print_helper(current.lChild, level + 1)

    def tree_info(self):
        if self.is_AVL:
            print("===== AVL TREE =====")
        else:
            print("===== BINARY SEARCH TREE =====")
        self.print()
        print("Tree height:", self.height())
        print("Tree range:", self.range())
        print("Values at level 2:", self.get_node_list_str(self.level(2)))
        print("Tree left side view:", self.get_node_list_str(self.left_side_view())) # line update 7/17
        print("Sum of leaf nodes:", self.sum_leaf_nodes())
        print()


''' DRIVER CODE '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open("tree.in")
    else:
        in_data = sys.stdin

    # Read input data
    line = in_data.readline().strip()
    line = line.split()
    tree_input = list(map(int, line)) 	# converts elements into ints

    # Create and print tree info for AVL Tree
    AVLtree = Tree(True)
    AVLtree.fill_tree(tree_input)
    AVLtree.tree_info()

    BSTtree = Tree(False)
    BSTtree.fill_tree(tree_input)
    BSTtree.tree_info()


if __name__ == "__main__":
    main()
