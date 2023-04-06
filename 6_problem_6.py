import random

# provided by Udacity
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


# provided by Udacity
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


# function takes linked lists as parameters
# outputs them in order of size
# in case of empty linked list replaces the list in the output by `None`
def measure_list(linked_list1, linked_list2):
    size1 = linked_list1.size()
    size2 = linked_list2.size()

    if size1 == 0 and size2 == 0:
        return None, None

    if size1 == 0:
        return linked_list2, None

    if size2 == 0:
        return linked_list1, None

    return (linked_list1, linked_list2) if size1 <= size2 else (linked_list2, linked_list1)


# takes two linked list as parameters
# outputs the union of the two linked lists as a linked list
def union(llist_1, llist_2):
   
    shorter_list, longer_list = measure_list(llist_1, llist_2)
    
    # if both lists are empty return None
    if not shorter_list and not longer_list:
        return None

    # go through the shorter list and add its values to the value_set 
    node = shorter_list.head
    value_set = {node.value}
    while node.next:
        value = node.next.value
        # remove node from list if the value it stores is a duplicate
        if value in value_set:
            node.next = node.next.next
        else:
            value_set.add(value)
            node = node.next
        
    # if the other list is empty return the list processed before
    if not longer_list:
        return shorter_list
        
    # add values from the other list to the modified first list
    node2 = longer_list.head
    while node2:
        if node2.value not in value_set:
            node.next = Node(node2.value)
            node = node.next
            # add value to value_set to make sure no duplicate values are strored from this list
            value_set.add(node2.value)
        node2 = node2.next
            

    return shorter_list

# TESTING UNION
print('\nTESTING UNION:\n')
print('Test Case 1')
print('testing to return "None" if both lists are empty')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('linked_list_1: ', linked_list_1)
print('linked_list_2: ', linked_list_2)    
print ('union: ', union(linked_list_1,linked_list_2))
# expected 'None'
    
print('\nTest Case 2:') 
print('testing with one empty list:')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [1, 2, 4, 4]
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
    
print('linked_list_1: ', linked_list_1)
print('linked_list_2: ', linked_list_2)    
print ('union: ', union(linked_list_1,linked_list_2))
# expected 1 -> 2 ->  4 -> 


# Test case 3 
# testing with to remove duplicates from longer list
print('\nTest Case 3')
print('testing with to remove duplicates from longer list')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [1, 2, 3, 3]
element_2 = [5, 5, 6, 6, 6]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
    
print('linked_list_1: ', linked_list_1)
print('linked_list_2: ', linked_list_2)    
print ('union: ', union(linked_list_1,linked_list_2))
# expected 1 -> 2 -> 3 -> 5 -> 6 ->


# Test case 4 
# testing with larger datasets
print('\nTest Case 4')
print('testing with larger datasets')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [random.randint(1, 1000000) for x in range(pow(10,3))]
element_2 = [random.randint(1, 1000000) for x in range(pow(10,3))]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
    
print('linked_list_1 first 10 element: ', element_1[:10])
print('linked_list_1 size: ', linked_list_1.size())
print('linked_list_2 first 10 element: ', element_2[:10])
print('linked_list_2 size: ', linked_list_2.size())
output_list = union(linked_list_1,linked_list_2)
print('union first 10 element: ')
node = output_list.head
for _ in range(10):
    print(node.value)
    node = node.next
print('size of union list: ', output_list.size())
# do not have expected result, but expect it to be done in less than forever time


# takes two linked list as parameters
# outputs the intersection of the two linked lists as a linked list
def intersection(llist_1, llist_2):
    
    shorter_list, longer_list = measure_list(llist_1, llist_2)
    
    # if any of the lists are empty return None
    if not shorter_list or not longer_list:
        return None
    
    # go through shorter list and add values to value_set
    node = shorter_list.head
    value_set = set()
    while node:
        value_set.add(node.value)
        node = node.next
    
    # check nodes in longer list and only keep them if they are commong non-duplicate values
    # gather common values in common_value set to help with eliminating duplicates
    common_values = set()
    
    # find new head for longer_list
    node = longer_list.head
    # setting next_node to head too, will change that when new head is found
    next_node = longer_list.head    
    
    while node and next_node == longer_list.head:
        # if the node is a common value add the value to common_values and keep it as head
        if node.value in value_set:
            common_values.add(node.value)
            # head is found change next_node to the next node
            next_node = node.next
        # if the node is not a common value check the next node
        else:
            longer_list.head = node.next
            node = longer_list.head
            next_node = longer_list.head

    # if there were no common values (no head was found return 'None')
    if not node:
        return None
        
    # check the rest of nodes in the list     
    while next_node:
        # if value is not common or already present in list drop the node from the list
        if next_node.value not in value_set or next_node.value in common_values:
            node.next = next_node.next
            next_node = node.next
        # if value is common and not a duplicate add its value to common_values
        # keep node in list
        # and move on to the next node
        else:
            common_values.add(next_node.value)
            node = next_node
            next_node = node.next
            
    return longer_list


# TESTING INTERSECTION
print('\n\nTESTING INTERSECTION:\n')
# Test Case 1
# testing to return 'None' if a list is empty
print('Test Case 1:')
print('testing to return "None" if a list is empty')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = []
element_2 = [5, 6, 7, 8]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('linked_list_1: ', linked_list_1)
print('linked_list_2: ', linked_list_2)    
print ('intersection: ', intersection(linked_list_1,linked_list_2))
# expected 'None'


# Test case 2 
# testing with no common values
print('\nTest Case 2')
print('testing with no common values')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [1, 2, 4, 4]
element_2 = [5, 6, 7]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
    
print('linked_list_1: ', linked_list_1)
print('linked_list_2: ', linked_list_2)    
print ('intersection: ', intersection(linked_list_1,linked_list_2))
# expected 'None'


# Test case 3 
# testing with common values and duplicates
print('\nTest Case 3')
print('testing with common values and duplicates')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [1, 2, 3, 3, 5, 4]
element_2 = [4, 5, 1, 3, 3, 3, 3, 3, 2]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
    
print('linked_list_1: ', linked_list_1)
print('linked_list_2: ', linked_list_2)    
print ('intersection: ', intersection(linked_list_1,linked_list_2))
# expected 4 -> 5 -> 1 -> 3 -> 2 ->


# Test case 4 
# testing with larger datasets
print('\nTest Case 4')
print('testing with larger datasets')
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [random.randint(1, 100000) for x in range(pow(10,3))]
element_2 = [random.randint(1, 100000) for x in range(pow(10,3))]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
    
print('linked_list_1 first 10 element: ', element_1[:10])
print('linked_list_1 size: ', linked_list_1.size())
print('linked_list_2 first 10 element: ', element_2[:10])
print('linked_list_2 size: ', linked_list_2.size())
output_list = intersection(linked_list_1,linked_list_2)
print('first 10 elements of intersection: ')
node = output_list.head
if not node:
    print('there were no common values')
for _ in range(10):
    print(node.value)
    node = node.next
    if not node:
        print('there are no more common values')
        break
print('size of intersection list: ', output_list.size())
# do not have expected result, but expect it to be done in less than forever time

