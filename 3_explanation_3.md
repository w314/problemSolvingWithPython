# Problem 3

## Huffman Encoding

### Time Complexity: `O(n)`
### Space Complexity: `O(n)`

### Explanation

`Time complexity`: For large input strings the encoding subtask has the most time complexity with `O(n)`, see explanation for subtasks below.

`Space complexity:` For large input strings the encoding subtask has the most space requirement, it's linear to the size of the input string, `O(n)` 


1. **Creating Huffman Table**
`Time Complexity`: `O(1)`
`Space Complexity`: `O(1)`
`Data Structure Used`: `dictionary`

`Time Complexity`: The function uses python's string.count() method to determine the frequency of each character, it takes `O(n)` to calculate it for each character. In worst case time complexity therefore could be `O(n^2)` for a small input string with different characters. However the functions uses a dictionary to store already counted characters, and it checks first if a character is new which takes constant time `O(1)`. As the number of different characters are limited, for large input strings time complexity is constant.

The space used for the dictinary depends on the size of the input string for small inputs. However as the size of the dictionary will never be larger than the number of different characters used for larger inputs the extra space needed for storing the dictionary is constant.


2. **Building Priority Queue**
`Time Complexity`: `O(1)`
`Space Complexity`: `O(1)`
`Data Structure Used`: `linked list`

`Time Complexity`: This function builds a linked list from the huffman table dictionary which is limited in size by the number of different characters used in the input string. For large input strings with 1.000.000 characters the input for this function is still under 1oo. Even if I expect to go through the whole list with each character to find it's place with time coplexity of O(n^2) = 1000, from the huffman encoding point of view for a large string input it's still constant time complexity `O(1)`
Space requeired for the linked list is based on the size of the huffman table which for the same reasons above from the point of the huffman encoding input string is constant.


3. **Building Huffman Tree**
`Time Complexity`: `O(1)`
`Space Complexity`: `O(1)`
`Data Structure Used`: `binary tree, linked list`

`Time Complexity`: This function builds binary tree from the elements of a linked list. The process involves traversing of the linked list to add new nodes. However as the number of elements in the linked list are limited by the number of different characters used in the input string for large input strings  it's still constant time complexity `O(1)`
Space requeired for the binary tree is based on the size of the huffman queue which - for the same reasons above - from the point of the huffman encoding input string is constant.


4. **Traversing Huffman Tree to Create Codes**
`Time Complexity`: `O(1)`
`Space Complexity`: `O(1)`
`Data Structure Used`: `binary tree, dictionary`

`Time Complexity`: This traverses a binary tree and adds codes to the huffman table dictionary. The size of the tree is limited by the number of different characters used in the input string. For large input strings  it's constant time complexity `O(1)`
There is no extra space requeirement for this subtask.


5. **Encoding Message**
`Time Complexity`: `O(n)`
`Space Complexity`: `O(n)`
`Data Structure Used`: `dictionary`

Time complexity depends on the length of input string as each character's code has to be looked up in the dictionary and added to the decoded string. As the codes are in a dictionary the lookup of the code of a character itself happens in constant time O(1). 
Space used also depends on the size of input string. The output string created will depend on length of the input string.



## Huffman Decoding

### Time Complexity: `O(n)`
### Space Complexity: `O(n)`
### Data Structure Used: `binary tree` 

### Explanation
Time compexity linear to the string to be decoded as all its characters has to be processed.
Space complexity is also linear to the size of the input string as a new string has to be build up.