# Problem 3 - Search in a Rotated Sorted Array

### Time Complexity: `O(nlogn)`
### Space Complexity: `O(n)`
### Algorithm Used: `merge sort`

### Explanation

`Time complexity`: I have used merge sort to sort the array, which had `O(nlogn)` time complexity. Also had to traverse the sorted array once,  which has `O(n)` time complexity. Approximately the whole process's time complexity is `O(nlogn)`. 

`Space complexity:` Merge sort has `O(n)` space complexity as the original input list is copied in the process. I have chosen merge sort over quick sort in this case as the time complexity was O(nlogn) in worst case. With quick sort if the pivot chosen is very bad, time complexity could have been worse than O(nlogn). However by chosing merge sort my space complexity is higher O(n), instead of O(1).

