def get_min_max(ints):
    """
    Finds the minimum and  maximum out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    Returns:
        min, max(tuple): minimum and maximum numbers in input array
    """
    
    # handle empty input array 
    if len(ints) == 0:
        return (None, None)
    
    # if input array contains just one value
    if len(ints) == 1:
        return (ints[0], ints[0])
    
    
    # set min and max numbers to the first number in input list
    min_num = ints[0]
    max_num = ints[0]
    
    # traverse input list and compare numbers to min and max numbers
    # update min and max numbers if smaller / larger values found
    for num in ints:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    
    return (min_num, max_num)

print('TESTING PROBLEM 6 (Min and Max in Unsorted Array)')

print('\nTest Case 1')
print('testing empty input array')
arr = []
print('input array: ', arr)
min_max = get_min_max(arr)
print('minimum and maximum of array: ', min_max)
# returns (None, None)

print('\nTest Case 2')
print('testing input array with one element')
arr = [3]
print('input array: ', arr)
min_max = get_min_max(arr)
print('minimum and maximum of array: ', min_max)
# returns (3, 3)

print('\nTest Case 3')
print('testing input array with same numbers')
arr = [5, 5, 5, 5]
print('input array: ', arr)
min_max = get_min_max(arr)
print('minimum and maximum of array: ', min_max)
# returns (5, 5)

print('\nTest Case 3')
print('testing input array with numbers in random order')
arr = [9, 2, 8, 8, 6, 7, 9]
print('input array: ', arr)
min_max = get_min_max(arr)
print('minimum and maximum of array: ', min_max)
# returns (2, 9)