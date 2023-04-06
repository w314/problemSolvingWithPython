# Problem 1

### Time Complexity: `O(logn)`
### Space Complexity: `O(logn)`
### Algorithm Used: `binary search, recursion`

### Explanation

`Time complexity`: I have used binary search to find the floored square root, by halving the number range to search the number in, it was possible to do it in `O(logn)` time.

`Space complexity:` The algorithm memory need depends on the number of rounds of recursions done during the binary search, larger numbers need more recursions. The number of recursions dependance on the input number is: `O(logn`).

