## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # set variable to store children
        self.children = {}
        # set variable to show if char stored here is the end of a word
        self.is_word = False
    
    def insert(self, char):
        # ads char to node's children
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        # variable to store all suffixes
        suffixes = list()
        
        # if the node coming is a word add suffix coming in the list of suffixes
        if self.is_word:
            suffixes.append(suffix)
        
        # check all children of node for a complete list of suffixes
        for key in self.children:
            suffixes.extend(self.children[key].suffixes(suffix + key))
                            
        # return list of suffixes
        # remove '' from suffixes list added in case the prefix itself was a word
        return suffixes[1:] if suffixes[0] == '' else suffixes    

        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        # start at the root
        node = self.root
        # for each char in word check if it's in the node's children
        for char in word:
            # if not add it to the node's children
            if char not in node.children:
                node.insert(char)
            node = node.children[char]
        # after adding all chars of word mark the node of the last char as is_word = True
        node.is_word = True
        
            
    def find(self, prefix):      
        ## Find the Trie node that represents this prefix
        
        # set node to root
        node = self.root
        
        # take each character of the prefix 
        # go through tree to find the char in the children of the current node
        # find node with prefix or declare it 'not found'
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return prefix + ' not found'

        # if node with prefix was foudn return the suffixes for that node                
        return node.suffixes()
            
        

print('TESTING PROBLEM 5 (Building a Trie)')

print('\nTest Case 1')
print('testing empty trie')
my_trie = Trie()
word_list = []
for word in word_list:
    my_trie.insert(word)
print('words in trie: ', word_list)
prefix = 'abc'
print('prefix: ', prefix)
suffixes = my_trie.find(prefix)
print('suffixes returned: ', suffixes)
# returns 'abc not found'

print('\nTest Case 2')
print('testing non_existent prefix in a non-empty trie')
my_trie = Trie()
word_list = ["ant", "factory", "trie"]
for word in word_list:
    my_trie.insert(word)
print('words in trie: ', word_list)
prefix = 'xy'
print('prefix: ', prefix)
suffixes = my_trie.find(prefix)
print('suffixes returned: ', suffixes)
# returns 'xy not found'

print('\nTest Case 3')
print('testing prefix that is not a word in itself')
my_trie = Trie()
word_list = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in word_list:
    my_trie.insert(word)
print('words in trie: ', word_list)
prefix = 'an'
print('prefix: ', prefix)
suffixes = my_trie.find(prefix)
print('suffixes returned: ', suffixes)
# returns ['t', 'thology', 'tagonist', 'tonym']

print('\nTest Case 4')
print('testing prefix that itself is a word')
my_trie = Trie()
word_list = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in word_list:
    my_trie.insert(word)
print('words in trie: ', word_list)
prefix = 'ant'
print('prefix: ', prefix)
suffixes = my_trie.find(prefix)
print('suffixes returned: ', suffixes)
# returns ['', 'hology', 'agonist', 'onym']