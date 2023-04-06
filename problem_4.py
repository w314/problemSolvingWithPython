def sort_012(input_list):
    """
    Given an input input_listay consisting on only 0, 1, and 2, sort the input_listay in a single traversal.

    Args:

       input_list(list): List to be sorted
    """
    
    # if lenght of array is 1 or smaller it's already sorted, return array
    if len(input_list) <= 1:
        return input_list
        
    # to keep track of the next index to place a '0'
    next0 = 0
    
    # to keep track of the next index to place a '2'
    next2 = len(input_list) - 1
    
    # current index 
    index = 0
    
    # when current index reaches next2 that's the last element to process
    while index <= next2:
        # current number to process
        num = input_list[index]
        
        # if the number is 1 nothing has to happen
        
        # if the number is '0' replace it with the number at the next0
        # it will be either a '0' if we are processing a first element and swapping it with itself
        # or it will be a '1', so no further actions needed
        if num == 0:
            # swap values
            input_list[index], input_list[next0] = input_list[next0], input_list[index]
            # increase next0 index
            next0 += 1
        # if the number to process is '2' it has to be moved to the next2 index    
        elif num == 2:
            # if number at next2 index is '2', set next2 to the first element not a '2'
            while input_list[next2] == 2:
                next2 -=1
                # if in the meantime we reach index it means our array is already sorted
                if next2 == index:
                    return input_list
            # swap out '2' to the value found at next2 place
            input_list[index], input_list[next2] = input_list[next2], input_list[index]
            # decrease next2 index
            next2 -= 1
            # if the number at the next2 place was a 0 move it the next0 index
            if input_list[index] == 0:
                # swap with next0
                input_list[index], input_list[next0] = input_list[next0], input_list[index]
                # increase next0 index
                next0 += 1                
        # increase index to process the next element in input_list    
        index += 1
        
    return input_list


    print('TESTING PROBLEM 4 (Dutch National Flag Problem)')

print('\nTest Case 1')
print('testing empty array')
arr = []
print('input array: ', arr)
sorted_array = sort_012(arr)
print('sorted array: ', sorted_array)
# returns []

print('\nTest Case 1')
print('testing array with one element')
arr = [0]
print('input array: ', arr)
sorted_array = sort_012(arr)
print('sorted array: ', sorted_array)
# returns [0]

print('\nTest Case 2')
print('testing array with "2"s only')
arr = [2, 2, 2]
print('input array: ', arr)
sorted_array = sort_012(arr)
print('sorted array: ', sorted_array)
# returns [2, 2, 2]

print('\nTest Case 3')
print('testing already sorted array')
arr = [0, 0, 1, 1, 2, 2]
print('input array: ', arr)
sorted_array = sort_012(arr)
print('sorted array: ', sorted_array)
# returns [0, 0, 1, 1, 2, 2]

print('\nTest Case 4')
print('testing unsorted array')
arr = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
print('input array: ', arr)
sorted_array = sort_012(arr)
print('sorted array: ', sorted_array)
# returns [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]