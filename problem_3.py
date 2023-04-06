def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    
    def merge_sort(arr):
        """
        Sorts array element in decreasing order.

        Args:
           arr(list): Input List
        Returns:
           sorted array(list)
        """
                    
        def merge(left, right):
            """
            Merges element from two list to create list with decreasing order.

            Args:
               left(list), right(list): input lists to merge
            Returns:
               merged sorted array(list)
            """

            output = list()
            left_index = 0
            right_index = 0
            
            # add elements from left or right array in decreasing order
            while left_index < len(left) and right_index < len(right):
                if left[left_index] >= right[right_index]:
                    output.append(left[left_index])
                    left_index += 1
                else:
                    output.append(right[right_index])
                    right_index += 1

            # add remaining elements to list (as only one half has elements, no need to compare)
            output += left[left_index :]
            output += right[right_index :]
            
            return output
            
            
        # base case, array with 1 or 0 elements is already sorted
        if len(arr) <= 1:
            return arr

        # find mid point
        mid_point = len(arr) // 2
        # sort left half of array
        left =  merge_sort(arr[:mid_point])
        # sort right half of array
        right = merge_sort(arr[mid_point:])

        # merge right and left part
        return merge(left, right)
        
        
     
    # handle empty input list:
    if len(input_list) == 0:
        return input_list
    
    # handle input list with 1 element
    if len(input_list) == 1:
        return [input_list[0], None]
    
    # handle input list with 2 elements:
    if len(input_list) == 2:
        return input_list
    
    
    # sort list
    sorted_array = merge_sort(input_list)

    # divide digits into two numbers
    output = [0, 0]    
    for index, item in enumerate(sorted_array):
        output[index % 2] = output[index % 2] * 10 + item

    return output


print('TEST PROBLEM 3 (rearange array elements)')

print('\nTest Case 1')
print('testing empty input list')
input_list = []
print('input list: ', input_list)
rearranged_list = rearrange_digits(input_list)
print('output: ', rearranged_list)
# returns []

print('\nTest Case 2')
print('testing input list with 1 element')
input_list = [3]
print('input list: ', input_list)
rearranged_list = rearrange_digits(input_list)
print('output: ', rearranged_list)
# returns [3, None]

print('\nTest Case 3')
print('testing input list with 2 elements')
input_list = [3, 4]
print('input list: ', input_list)
rearranged_list = rearrange_digits(input_list)
print('output: ', rearranged_list)
# returns [3, 4]

print('\nTest Case 4')
print('testing input list with odd elements')
input_list = [3, 4, 7]
print('input list: ', input_list)
rearranged_list = rearrange_digits(input_list)
print('output: ', rearranged_list)
# returns [73, 4]

print('\nTest Case 5')
print('testing input list with even elements')
input_list = [4, 6, 2, 5, 9, 8]
print('input list: ', input_list)
rearranged_list = rearrange_digits(input_list)
print('output: ', rearranged_list)
# returns [964, 852]