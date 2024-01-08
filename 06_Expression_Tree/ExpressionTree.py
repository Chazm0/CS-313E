#  File: ExpressionTree.py
#  Student Name: Zimo Chen
#  Student UT EID: zc5983

import sys

# list of valid operators
operators = ['+', '-', '*', '/', '//', '%', '**']


# Input: Elements of a simple expression
#        operator (String) and two operands (numbers)
# Output: result of evaluation of the expression
def operation(operator, n, m):
    expression = str(n) + operator + str(m)
    return eval(expression)


# Stack Class - DO NOT CHANGE
# Traditional Stack implementation containing list of data items
# Used to keep track of items in nested expressions.
class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


# Node Class
# Purpose: Used by the Tree Class to represent one operand or operators
#          in a binary expression. It includes data (a character) and
#          two pointers, to the left and right child nodes.
# You do not need to make changes to this class.
class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


# Tree Class
# Purpose: To represent the string representation of operators and operands
#          of a binary expression so it can be evaluated.
# You need to make a lot Of changes to this class!
class Tree (object):
    def __init__(self):
        self.root = Node(None)

    # Input: a string expression
    # Output: an expression tree
    def create_tree(self, expr):
            stack = Stack()
            operator_stack = Stack()

            tokens = expr.split()
            for token in tokens:
                if token.isdigit() or '.' in token:
                    try:
                        if '.' in token:
                            number = float(token)
                        else:
                            number = int(token)
                        # print(f"Creating leaf node with data: {number}")
                        stack.push(Node(data=number))
                    except ValueError:
                        print(f"Invalid number: {token}")
                elif token in operators:
                    # print(f"Creating operator node with data: {token}")
                    while (not operator_stack.is_empty() and operator_stack.peek().data in operators and
                        operators.index(operator_stack.peek().data) <= operators.index(token)):
                        stack.push(self._create_subtree(operator_stack.pop(), stack.pop(), stack.pop()))
                    operator_stack.push(Node(data=token))
                elif token == '(':
                    operator_stack.push(Node(data=token))
                elif token == ')':
                    while operator_stack.peek().data != '(':
                        stack.push(self._create_subtree(operator_stack.pop(), stack.pop(), stack.pop()))
                    operator_stack.pop()

            while not operator_stack.is_empty():
                stack.push(self._create_subtree(operator_stack.pop(), stack.pop(), stack.pop()))

            self.root = stack.pop()
            # print(f"Root of the tree is set with data: {self.root.data}")

    def _create_subtree(self, operator_node, right_node, left_node):
        operator_node.lChild = left_node
        operator_node.rChild = right_node
        return operator_node


    # Input: A node in an expression tree
    # Output: The result of evaluating the expression
    #         with this node as the root
    def evaluate(self, current):
        if current.lChild is None and current.rChild is None:
            # print(f"Leaf Node: {current.data}")
            return float(current.data)
        else:
            left_value = self.evaluate(current.lChild)
            right_value = self.evaluate(current.rChild)
            # print(f"Current Node: {current.data}, Left Child Result: {left_value}, Right Child Result: {right_value}")
            return operation(current.data, left_value, right_value)
        

    # Starter Method for pre_order
    # Input: a node in an expression tree
    # Output: (string) the preorder notation of the expression
    #                  with this node a the root
    def pre_order(self, current):
        if current is None:
            return ""
        result = str(current.data) + " "
        result += self.pre_order(current.lChild)
        result += self.pre_order(current.rChild)
        return result

    # Starter Method for post_order
    # Input: a node in an expression tree
    # Output: (string) the post order notation of the expression
    #                  with this node a the root
    def post_order(self, current):
        if current is None:
            return ""
        result = self.post_order(current.lChild)
        result += self.post_order(current.rChild)
        result += str(current.data) + " "
        return result


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('expression.in')
    else:
        in_data = sys.stdin

    # read infix expression
    line = in_data.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    # print(expr)
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
