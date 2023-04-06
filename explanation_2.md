# Problem 4

### Time Complexity: `O(n)`
### Space Complexity: `O(n)`
### Algorithm Used: `recursion`

### Explanation

`Time complexity`: To find all files the algorithm has to  look through all files and subdirectories once. Therefore time comlexity is linear `O(n)`, it depends on the number of files and subdirectories found under the path given as parameter.

`Space complexity:` In worst case all files in all subdirectories have the suffix given as the parameter and all have to be stored in the output list. Therefore space complexity depends on the number of files found under path given as parameter.

I have used recursion as it was an effective way to look through all the subdirectories and their subdirectories. The task demanded to do the same subtasks (checking files and directories) again and again down the hieararchy. Recursion was a good fit for the task.
