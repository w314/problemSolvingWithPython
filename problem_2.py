def search_index_of_smallest(arr, start_index, end_index):
    """
    Find the index by of the smallest number in the array (assuming there are no duplicates in array)

    Args:
        arr(array): input array
        start_index(int): first index of array part of search as in:  arr[start_index : end_index+1]
        end_index(int): last index of array part of search as in: arr[start_index : end_index+1]
    Returns:
       int: Index
    """
    
    # base cases
    # if the array to search has one element only the first element of the array is the smallest
    if start_index == end_index:
        return 0
    # if the array to search has two elements
    # if they are in increasing order the first element of the array is the smallest
    # if they pivot, return the index of the pivoted element
    if start_index == end_index - 1:
        return end_index if arr[end_index] < arr[start_index] else 0
    
    
    # find mid-point in array
    mid_point = start_index + (end_index - start_index) // 2
    
    # if array is pivoted after mid-point return index of element after mid-point
    if arr[mid_point] > arr[mid_point + 1]:
        return mid_point + 1
    #if array is pivoted at mid-point return index of mid-point
    elif arr[mid_point] < arr[mid_point - 1]:
        return mid_point
    
    # search in array after mid-point
    return search_index_of_smallest(arr, mid_point + 2, end_index)
    # search in array before mid-point
    return search_index_of_smallest(arr, start_index, mid_point - 2)


def binary_search(arr, start_index, end_index, number):
    """
    Find the index by of number in the part of array defined the start_index, end_index

    Args:
        arr(array): input array
        start_index(int): first index of array part of search as in:  arr[start_index : end_index+1]
        end_index(int): last index of array part of search as in: arr[start_index : end_index+1]
        number(int): target number to find the index of
    Returns:
       int: Index or -1
    """
     
    # if array is empty return -1 for not found    
    if len(arr[start_index: end_index + 1]) == 0:
        return -1
    
    # select mid_point
    mid_point = start_index + (end_index - start_index) // 2

    # if number is found return mid_point
    if arr[mid_point] == number:
        return mid_point
    
    # if number is larger than mid_point search in end of array
    if arr[mid_point] < number:
        return binary_search(arr, mid_point + 1, end_index, number)
    # if number is smaller than mid_point search in first part of arary
    else:
        return binary_search(arr, start_index, mid_point - 1, number)    


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # check for empty input array
    if len(input_list) == 0:
        print('empty input array')
        return -1

    # find index of smallest element
    smallest_element_index = search_index_of_smallest(arr, 0, len(input_list) - 1)
    # set last pivoted element
    last_pivoted_element = input_list[-1]
    
    # if number is larger than last pivoted element search in array before pivot
    if number > last_pivoted_element:
        return binary_search(input_list, 0, smallest_element_index, number)
    # if number is equal or smaller than last pivoted element search in pivoted part of array
    else:
        return binary_search(input_list, smallest_element_index, len(input_list) - 1, number)



print('TESTING PROBLEM 2 (search in sorted rotated array)')

print('\nTest Case 1')
print('testing empty array')
arr = []
target = 3
print('input list: ', arr)
print('number to search for: ', target)
index = rotated_array_search(arr, target)
print('index returned: ', index)
# prints message 'empty input array', returns -1

print('\nTest Case 2')
print('testing search for number not in array')
arr = [5, 6, 4]
target = 3
print('input list: ', arr)
print('number to search for: ', target)
index = rotated_array_search(arr, target)
print('index returned: ', index)
# returns -1


print('\nTest Case 3')
print('testing search for number in non-pivoted array')
arr = [1, 2, 3, 4, 5]
target = 3
print('input list: ', arr)
print('number to search for: ', target)
index = rotated_array_search(arr, target)
print('index returned: ', index)
# returns 2

print('\nTest Case 4')
print('testing search for number in pivoted array right before pivot')
arr = [10, 11, 12, 1, 2, 3, 4, 5]
target = 12
print('input list: ', arr)
print('number to search for: ', target)
index = rotated_array_search(arr, target)
print('index returned: ', index)
# returns 2

print('\nTest Case 5')
print('testing search for number in pivoted array at pivot')
arr = [10, 11, 12, 1, 2, 3, 4, 5]
target = 1
print('input list: ', arr)
print('number to search for: ', target)
index = rotated_array_search(arr, target)
print('index returned: ', index)
# returns 3

print('\nTest Case 6')
print('testing search for number in pivoted for first element')
arr = [10, 11, 12, 1, 2, 3, 4, 5]
target = 10
print('input list: ', arr)
print('number to search for: ', target)
index = rotated_array_search(arr, target)
print('index returned: ', index)
# returns 0

print('\nTest Case 7')
print('testing search for number in pivoted for last element')
arr = [10, 11, 12, 1, 2, 3, 4, 5]
target = 5
print('input list: ', arr)
print('number to search for: ', target)
index = rotated_array_search(arr, target)
print('index returned: ', index)
# returns 7