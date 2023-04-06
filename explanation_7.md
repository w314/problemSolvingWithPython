# Problem 7 - HTTPRouter

### Time Complexity: `O(n*c)` (where n = the legth of the path array  and c = number of children in each node)
### Space Complexity: `O(c^d)` (where c = number of children in each node, d depth of trie)
### Data Strucutures, Algorithms Used: `tree, dictionary`

### Explanation

`Time complexity`: 
To finding or inserting a handler,  the time complexity is `O(n * c)`. For each element of the path aray (n) we have to look for all the children of the node we are working on (c).

`Space complexity:` The amount of memory needed depends on the amount of information stored in the trie. The space needed is c * c * c .... where c is the number of children in each node. To summarize it's `O(c^d)` where c is the size of the character set used, and d is the depth of the trie.