# Problem 5 - Building Trie

### Time Complexity: `O(n^d)` (where n = size of character set used, d depth of trie)
### Space Complexity: `O(n^d)` (where n = size of character set used, d depth of trie)
### Data Strucutures, Algorithms Used: `tree, dictionary, recursion`

### Explanation

`Time complexity`: 
To insert a word time complexity is: `O(n*c)` where n is the length of the word to insert and c is the size of character set we use.
To find suffixes we first find the prefix. 
Finding a prefix has `O(n*c)` time complexity where n is the length of the prefix and c is the size of the character set we use.
To find the suffixes for a given prefix we have to go through all the children of the node of the prefix and their children and their children... Time complexity is `O(c^d)` where c is the size of the character set we use (= maximum number of children a node can have) and d is the depth of the trie.
This makes the time complexity of finding suffixes O((n * c) + (c^d)) which approximates to `O(c^d)`


`Space complexity:` The amount of memory needed depends on the amount of information stored in the trie. As each node can have the whole character set (c) as it's children and all of those children can have the whole character set as children and so forth, the space needed is c * c * c .... depending the depth of the trie. 
The trie's scpace complexity therefore `O(c^d)` where c is the size of the character set used, and d is the depth of the trie.

