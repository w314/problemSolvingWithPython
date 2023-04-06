def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    
    def find_sqrt(min_num, max_num, number):
        """
        Uses binary search to find floored square root of 'number

        Args:
            min_num(int): Minimum number of the number range to search the square root in
            max_num(int): Maximum number of the number range to search the square root in
            number(int): Number to find the floored squared root of
        Returns:
           int: Floored Square Root or -1 if input parameter is invalid
        """    
        
        # if there is one number left to check return the number
        if min_num == max_num:
            return min_num          
        
        # calculate middle of number range (mid_point) and it's square
        mid_point =  min_num + (max_num - min_num) // 2
        square = mid_point * mid_point
        
        # if square equals the number return mid_point
        if square == number:
            return mid_point
        
        # if square is smaller than the number
        if mid_point * mid_point < number:
            # if there is only one number higher then mid_point in number range check the squre of that number
            # it is necessary to catch floored square roots
            # if next number's square is too high return mid_point
            if min_num == max_num - 1 and max_num * max_num > number:
                return min_num
            # otherwise search in the remaining number range above mid_point
            else:
                return find_sqrt(mid_point + 1, max_num, number)
        # if squre is larger than number search the remaining number range below mid point 
        else:
            return find_sqrt(min_num, mid_point - 1, number)
    
    # check if input parameter is integer
    if not isinstance(number, int):
        print('Input has to be an integer')
        return -1
    
    # check if input parameter is non-negative
    if number < 0:
        print('Input has to be non-negative integer.')
        return -1
        
    # if number is 0 or 1 return number itself    
    if number == 0 or number == 1:
        return number
    
    # use binary sort to find squre root for number 2 and above
    return find_sqrt(2, number, number)


print('TESTING PROBLEM 1 (floored square root)')

print('\nTest Case 1')
print('testing non-integer input number')
number = ''
print('input number: ', number)
floored_square_root = sqrt(number)
print('floored square root returned: ', floored_square_root)
# print message 'Input has to be an integer', returns -1

print('\nTest Case 2')
print('testing negative input number')
number = -2
print('input number: ', number)
floored_square_root = sqrt(number)
print('floored square root returned: ', floored_square_root)
# print message 'Input has to be a non-negatvie integer', returns -1

print('\nTest Case 3')
print('testing 0')
number = 0
print('input number: ', number)
floored_square_root = sqrt(number)
print('floored square root returned: ', floored_square_root)
# returns 0

print('\nTest Case 4')
print('testing 1')
number = 1
print('input number: ', number)
floored_square_root = sqrt(number)
print('floored square root returned: ', floored_square_root)
# returns 1


print('\nTest Case 5')
print('testing perfect square')
number = 25
print('input number: ', number)
floored_square_root = sqrt(number)
print('floored square root returned: ', floored_square_root)
# returns 5


print('\nTest Case 6')
print('testing imperfect square')
number = 27
print('input number: ', number)
floored_square_root = sqrt(number)
print('floored square root returned: ', floored_square_root)
# returns 5


print('\nTest Case 7')
print('testing large input number')
number = 746274524184048846
print('input number: ', number)
floored_square_root = sqrt(number)
print('floored square root returned: ', floored_square_root)
# returns 863871821