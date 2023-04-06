# Problem 2 - Search in a Rotated Sorted Array

### Time Complexity: `O(logn)`
### Space Complexity: `O(logn)`
### Algorithm Used: `binary search, recursion`

### Explanation

`Time complexity`: I have used binary search to find the smallest element of the array to know the index the array is pivoted. I have also used binary search to search for the target in the appropriate section of the input array. Using binary search made it possible to find the target in  `O(logn)` time.

`Space complexity:` The algorithm memory need depends on the number of elements in the input list, larger input lists need more recursions. The number of recursions dependance on the length of the input array is: `O(logn`).

