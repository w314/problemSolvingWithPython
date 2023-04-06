# Problem 1

### Time Complexity: `O(1)`
### Space Complexity: `O(n)`
### Data Structure Used: `maps (dictionaries)`

### Explanation

`Time complexity`: I have used a dictionary to store the values of the items stored in the cache as well as a the keys to the next and previous element in the usage order. This dictionary and two variables were I have stored the most and least recently used items allowed the get and set functions to work in constant time `O(1)`.
(Keeping the items in any kind of list in the order of usage would have requeired transversing some or all of the list when updating the order,  with time complexity of O(n))

`Space complexity:` space used depends on the capacity of the cache
