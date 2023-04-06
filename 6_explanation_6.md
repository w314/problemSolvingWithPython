# Problem 6

## Union

### Time Complexity: `O(n)`
### Space Complexity: `O(n)`
### Data Structure Used: `set`

### Explanation

`Time complexity`: As I have to go through all the nodes time complexity depends on the size of the input linked lists: `O(n)`

`Space complexity:` Using the set adds extra space requirement, worst case - with no duplicates at all - the set will be the size of the size of the two linked lists

- I've used a set to store all unique values from the first list. Having a set helped me determine if a node's value is duplicate or a new one.
- While going through all the nodes I've removed those which had duplicate values.
- I've decided to modify the first list and use it as my output list (not creating a new one from scrath and add values as I identify them) to save space. 
- After processing the first list, I went through all the nodes of the second list. Used the set to check if any values are new.
- In case of new values I've added a node with the value to the old list and the value to the set.



## Intersection

### Time Complexity: `O(n)`
### Space Complexity: `O(n)`
### Data Structure Used: `set`

### Explanation

`Time complexity`: As I have to go through all the nodes time complexity depends on the size of the input linked lists: `O(n)`

`Space complexity:` Using the sets adds extra space requirement, worst case - with both linked lists having the same values without duplicates - the sets will be the size of the size of the two linked lists

- I've used a set to store all unique values from the shorter list. Having a set helped me determine if a node's value is duplicate or a new one.
- I have started with the shorter list to save space as all the values of the first list goes to the set, but none from the second.
- After processing the first list, I went through all the nodes of the second list. Used the first set to check if any values are common with the first list. I have created an other set here to store the common values to help determine if any common value is newly found or a duplicate value.
- I've decided to modify the second list and use it as my output list (not creating a new one from scrath and add values as I identify them) to save space. 
- As I processed the second list I dropped any nodes with uncommon or duplicate common values and returned the modified second list as my output.

