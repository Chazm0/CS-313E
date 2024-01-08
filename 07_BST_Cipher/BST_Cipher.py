#  File: BST_Cipher.py
#  Student Name: Zimo Chen
#  Student UT EID: zc5983

import sys

# One node in the BST Cipher Tree


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None


# The BST Cipher Tree
class Tree:

    # Create the BST Cipher tree based on the key
    def __init__(self, key):
        # This is for debug purposes only.
        # Comment out or delete before submitting.
        # key_tree.BST_print()
        self.root = None
        for ch in self.clean(key):
            self.insert(ch)


    # Insert one new charater/Node to the BST Cipher tree
    # If the character already exists, don't add it.
    def insert(self, ch):
        if self.root is None:
            self.root = Node(ch)
            return
        node = self.root
        while node:
            prev_node = node
            if ch < node.ch:
                node = node.left
            elif ch > node.ch:
                node = node.right
            else:
                return  
        if ch < prev_node.ch:
            prev_node.left = Node(ch)
        else:
            prev_node.right = Node(ch)

    # Encrypts a text message using the BST Tree
    def encrypt(self, message):
        message = self.clean(message)
        encrypted_message = '!'.join([self.encrypt_ch(ch) for ch in message])
        # Check if there is a space in the Message to Decrypt
        if ' ' in message:
            encrypted_message = '*' + encrypted_message
        return encrypted_message

    # Encrypts a single character
    def encrypt_ch(self, ch):
        node = self.root
        path = ''
        while node:
            if ch < node.ch:
                path += '<'
                node = node.left
            elif ch > node.ch:
                path += '>'
                node = node.right
            else:
                return path

    # Decrypts an encrypted message using the BST Tree
    def decrypt(self, codes_string):
        codes = codes_string.split('!')
        return ''.join([self.decrypt_code(code) for code in codes])

    # Decrypts a single code
    def decrypt_code(self, code):
        node = self.root
        for direction in code:
            if node is None:
                return ''
            if direction == '<':
                node = node.left
            elif direction == '>':
                node = node.right
        return node.ch if node else ''

    # Get printed version of BST for debugging
    def BST_print(self):
        if self.root is None:
            return "Empty tree"
        self.BST_print_helper(self.root)

    # Prints a BST subtree
    def BST_print_helper(self, node, level=0):
        if node is not None:
            if node.right is not None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left is not None:
                self.BST_print_helper(node.left, level + 1)

    def clean(self, text):
        cleanText = ""
        for i in range(len(text)):
            if (self.isValidCh(text[i])):
                cleanText += text[i]
        return cleanText

    # Utility method
    def isValidLetter(self, ch):
        if (ch >= "a" and ch <= "z"):
            return True
        return False

    # Utility method
    def isValidCh(self, ch):
        if (ch == " " or self.isValidLetter(ch)):
            return True
        return False


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # read string to be encrypted
    text_message = in_data.readline().strip()

    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()
