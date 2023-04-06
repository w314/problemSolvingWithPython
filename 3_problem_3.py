# node class for huffman priority queue nodes
class Node:
    def __init__(self, letter, frequency, prev_node = None, next_node = None):
        self.letter = letter
        self.frequency = frequency
        self.prev = prev_node
        self.next = next_node



# class for huffman priority queue linked list
class HuffmanLink:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
     
    # adds a new node
    def add_node(self, letter, frequency):
        
        self.size += 1
        
        # if queue is empty
        if not self.head:
            self.head = Node(letter, frequency)
            self.tail = self.head
            return
        
        # if new frequency belongs to the end    
        if frequency >= self.tail.frequency:
            node = Node(letter, frequency, self.tail, None)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            return

        
        # if new frequency belongs to the beginning 
        if frequency <= self.head.frequency:
            node = Node(letter, frequency, None, self.head)
            self.head.prev = node
            self.head = node
            return
            
        
        # find rigth place for the frequency
        node = self.head
        next_node = self.head.next
        while frequency >= next_node.frequency:
            node = node.next
            next_node = next_node.next
        # add new node to the list
        new_node = Node(letter, frequency, node, next_node)
        node.next = new_node
        next_node.prev = new_node
 

    # removes the two minumum frequency nodes from the queu
    # adds a new node with None as letter and the sum of the two minimum frequencies as frequency
    def merge_nodes(self):
            
        # get the first two minimum frequency nodes
        if not self.head:
            return None, None
        
        if not self.head.next:
            return self.head, None
        
        node1 = self.head
        node2 = self.head.next
        
        # create output 
        left_node = {
            'letter': node1.letter,
            'frequency': node1.frequency
        }
        right_node = {
            'letter' : node2.letter,
            'frequency' : node2.frequency
        }
        
        
        # reset queue size
        self.size -= 2
        
        # if queue is now empty reset head and tail
        if self.size == 0:
            self.head = None
            self.tail = None
            return left_node, right_node 
        
        # reset head
        self.head = node2.next
        self.head.prev = None
        
        # add new node to queue
        self.add_node(None, node1.frequency + node2.frequency)
        
        # return two miminum nodes
        return left_node, right_node

        
    # prints letter and frequency of each node in queue        
    def print_queue(self):
        node = self.head
        output = ''
        while node:
            output += node.letter + ':' + str(node.frequency) + ' '
            node = node.next
        print(output)



# class for huffman tree nodes
class TreeNode:
    def __init__(self, letter, frequency, left = None, right = None):
        self.letter = letter
        self.frequency = frequency
        self.left = left
        self.right = right

        

# class for huffman tree binary tree        
class HuffmanTree:
    def __init__(self):
        self.root = None



# class for stack nodes used when traversing huffman tree
class Status:
    def __init__(self, node, left_visited = None, right_visited = None):
        self.letter = node.letter
        self.frequency = node.frequency
        self.left = node.left
        self.right = node.right
        self.left_visited = left_visited
        self.right_visited = right_visited



# huffman encoding algorithm        
def huffman_encoding(string):
    
    def build_huffman_table():
        huffman_table = {}
        for letter in string:
            if letter not in huffman_table:
                huffman_table[letter] = {'frequency' : string.count(letter)}
        return huffman_table
 

    def build_priority_queue():
        
        queue = HuffmanLink()
        
        for k, v in huffman_table.items():
            queue.add_node(k, v['frequency'])
        
        return queue
        
        
    def build_huffman_tree():
        
        # will store frequency with an array of nodes which have that frequency
        tree_nodes = {}
        huffman_tree = HuffmanTree()
        
        if queue.size == 0:
            return huffman_tree
         
        if queue.size == 1:
            node = queue.head
            huffman_tree.root = TreeNode(node.letter, node.frequency, None, None)
            return huffman_tree
            
        
        
        # takes a letter and frequency and creates child node to use for huffman tree
        def create_child_node(letter, frequency):           
            # if letter == 'None', information is from  an internal node
            if not letter:
                # use node stored in tree_nodes dicionary
                child_node = tree_nodes[frequency][-1]
                # delete used node from dictionary
                # if there are several nodes with the same frequency delete the node from value-array
                if len(tree_nodes[frequency]) > 1:
                    tree_nodes[frequency] = tree_nodes[frequency][:-1]
                # if it had only one node with given frequency delete frequency key
                else:
                    del(tree_nodes[frequency])
            # if  it is leaf (letter is value) create node for it
            else:
                child_node = TreeNode(letter, frequency)
             
            return child_node                
        
        while queue.size > 0:
            # remove the two minimum nodes
            left_child, right_child = queue.merge_nodes()

            # create tree node for left child
            left_node = create_child_node(left_child['letter'], left_child['frequency'])
            
            # create tree node for right child
            right_node = create_child_node(right_child['letter'], right_child['frequency'])
            
            # create parent node of children
            parent_node = TreeNode(None, left_node.frequency + right_node.frequency, left_node, right_node)

            # add created parent node to tree_nodes dictionary
            # if frequency is already present in tree_nodes add parent_node to value array
            if parent_node.frequency in tree_nodes:
                value_array = tree_nodes[parent_node.frequency]
                value_array.append(parent_node)
                tree_nodes[parent_node.frequency] = value_array
            else:
                tree_nodes[parent_node.frequency] = [parent_node]
            
        # get last item from tree_nodes dictionary
        for k, v in tree_nodes.items():
            node = v[0]
        # assign it as the root of the huffman tree
        huffman_tree.root = node
        
        return huffman_tree    
    
    
    def add_code_to_huffman_table():
        
        # if tree is empty
        if not huffman_tree.root:
            return 'Huffman Tree is empty'

        # if tree has only a root
        if not (huffman_tree.root.left or huffman_tree.root.right):
            # add code to Huffman Table
            huffman_table[huffman_tree.root.letter]['code'] = '0'
            return

        node = huffman_tree.root
        stack = list()
        status = Status(node)
        stack.append(status)
        code = ''
        while len(stack) > 0:
            node = stack[-1]
            
            # if node is leaf
            if node.letter:
                # add code to huffman table
                huffman_table[node.letter]['code'] = code
                # remove node from stack
                stack.pop()
                # delete last digit form code
                code = code[:-1]
                continue
            
            # if node is parent and has unvisited left child
            if node.left and not node.left_visited:
                # add '0' to code
                code += '0'
                # set left_visited to True
                node.left_visited = True
                # add left node to stack
                status = Status(node.left)
                stack.append(status)
                continue
                
            # if node is parent and has unvisited right child    
            if node.right and not node.right_visited:
                # add '1' to code
                code += '1'
                # set right_visited to True
                node.right_visited = True
                # add right node to stack
                status = Status(node.right)
                stack.append(status)
                continue
                
            # if node is parent and all children are visited already
            # remove from stack
            stack.pop()
            # remove last digit from code
            code = code[:-1]
            
            
    def encode_message():
        encoded_message = ''
        for letter in string:
            encoded_message += huffman_table[letter]['code']
        return encoded_message
        
        
    # if input string is empty return 'None' both for encoded message and huffman tree  
    if len(string) == 0:
        print('Input string is empty')
        return None, None
    
    huffman_table = build_huffman_table()
    # print('huffman table: ')
    # print(huffman_table)
    queue = build_priority_queue()
    # print('huffman priority queue: ')
    # queue.print_queue()
    huffman_tree = build_huffman_tree()
    # print('huffman tree root: ')
    # print(huffman_tree.root.letter, huffman_tree.root.frequency)
    add_code_to_huffman_table()
    # print('huffman table with codes:')
    # for k, v in huffman_table.items():
    #     print(k, v)
    #     print(type(k), type(v))
    encoded_message = encode_message()
    # print('encoded message:')
    # print(encoded_message)
    return encoded_message, huffman_tree
    
            
            
# huffman decoding algorithm           
def huffman_decoding(coded_message, huffman_tree):
    
    if not (coded_message or huffman_tree):
        print('Invalid input')
        return None
    
    node = huffman_tree.root
    decoded_message = ''

    # if huffman tree consists of only a root, message had only 1 character
    if not (node.left or node.right):
        letter = node.letter
        for code in coded_message:
            decoded_message += letter
        return decoded_message

    
    # in case of regular message with several characters
    # process each code in message
    for code in coded_message:
        if code == '0':
            node = node.left
        else:
            node = node.right
        
        # if leaf is found add letter to decoded_message
        if node.letter:
            decoded_message += node.letter
            # restart decoding from root of the tree
            node = huffman_tree.root
    
    return decoded_message
        


# TESTING HUFFMAN CODING
import sys

print('\nTESTING HUFFMAN CODING')
print('\nTest Case 1:')
print('testing with empty string')
string = ''
print('\nEncoding Input:')
encoded_data, tree = huffman_encoding(string)
print(encoded_data, tree)
# expects 'Input string is empty' message and returns: None', 'None'
print('\nDecoding Input:')
decoded_data = huffman_decoding(encoded_data, tree)
print(decoded_data)
# expects 'Invalid input' message, returns: None'

print('\nTest Case 2:')
print('testing with 1 character')
# string = 'A'
a_great_sentence = "a"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)




print('\nTest Case 3:')
print('testing with string of the same character')
# string = 'A'
a_great_sentence = "aaaaaaaaaaaaaaaaaa"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)



print('\nTest Case 4:')
print('testing with regular string\n')

a_great_sentence = "The bird is the word"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))


print('\nTest Case 5:')
print('testing with long string\n')

import random

char_array = [chr(random.randint(65, 125)) for x in range(pow(10,6))]
# print(char_array)
a_great_sentence = ''.join(char_array)
# print(a_great_sentence)

# a_great_sentence = "The bird is the word"
print("The length of the input string is: {}\n".format(len(a_great_sentence)))
print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The first 50 character of the data is: {}\n".format(a_great_sentence[:50]))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The first 50 character of the encoded data is: {}\n".format(encoded_data[:50]))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The first 50 character of the encoded data is: {}\n".format(decoded_data[:50]))
