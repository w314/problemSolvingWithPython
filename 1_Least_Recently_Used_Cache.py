class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if capacity <= 0:
            print('Invalid capacity')
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.latest = None
        self.oldest = None 
        
    
    # removes oldest element form cache order and resets self.oldest
    # does not delet oldest element
    def __remove_oldest__(self):
        # set oldest to the next item
        self.oldest = self.cache[self.oldest]['next']
        # set new oldest's prev attribute to None
        self.cache[self.oldest]['prev'] = None    
        
    # adds element to cache    
    def __add_item__(self, key, value):
        # add value to cache
        self.cache[key] = {
            'value' : value,
            'prev' : self.latest,
            'next' : None
        }
        
    # gets value if key is in cache, returns -1 if key is not in cache
    def get(self, key):

        # if key is not in cache return -1
        try:
            output = self.cache[key]['value']
        except:
            return -1
        
        
        # update cache order
        
        # if item was the latest, order is still correct, return value
        if self.latest == key:
            return output
        

        # update chain of links in cache order
        # if item was oldest:
        if self.oldest == key:
            self.__remove_oldest__()
        # if it was an item in the middle
        else:
            self.cache[self.cache[key]['prev']]['next'] = self.cache[self.cache[key]['next']]
        # set the key's next attribute to None
        self.cache[key]['next'] = None
        # set the key's prev attribute to what used to be the latest
        self.cache[key]['prev'] = self.latest
        # set key at the end of the order
        self.cache[self.latest]['next'] = key
        # put this item as most recently used
        self.latest = key
        
        return output
        

    # sets value to cache if not already there
    def set(self, key, value):
        
        # Set the value if the key is not present in the cache.
        if key not in self.cache:
            # if there is still capacity add item
            if self.size < self.capacity:
                self.__add_item__(key, value)
                # increase cache size
                self.size += 1
            # if cache if full remove least recently used item
            else:
                if self.capacity <= 0:
                    print('Cache does not work properly as it has invalid capacity: ', self.capacity)
                    return
                key_to_delete = self.oldest
                # remove oldest item from cache order
                self.__remove_oldest__()
                # delete oldest item from cache
                del(self.cache[key_to_delete])
                # add incoming item to cache
                self.__add_item__(key, value)
                
        
            # if it's the first element added update oldest:
            if not self.oldest:
                self.oldest = key
            # update next parameter of the used to be latest element
            if self.latest:
                self.cache[self.latest]['next'] = key
            # set latest attribute to value just added
            self.latest = key


# TESTING LRU CACHE
print('\nTESTING LRU CACHE')

#Test Case 1
# testing invalid cache size
print('\nTest Case 1')
print('testing invalid cache size: -3')
our_cache = LRU_Cache(-3)
# print(our_cache)
# prints 'invalid cache size' returns 'None'
our_cache.set(1, 1);
# prints 'Cache does not work properly as it has invalid capacity: ' + prints capacity
print(our_cache.get(3))
# returns -1

#Test Case 2
# testing cache put
print('\nTest Case 2')
print('testing cache put')
our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
our_cache.set(5, 5) 
print(our_cache.size)
# returns 5

#Test Case 3
# testing cache hit
print('\nTest Case 3')
print('testing cache hit')
print(our_cache.get(3))
# returns 3

print('\nTest Case 4')
# testing cache miss
print('testing cache miss')
print(our_cache.get(9))
# returns -1

print('\nTest Case 5')
# testing cache put at full capacity
print('testing cache put at full capacity')
our_cache.set(6, 6)
print(our_cache.get(1))
# returns -1 as 1 was removed when setting 6


print('\nTest Case 6')
# testing cache put at full capacity
print('testing cache keeps least recently used order properly')
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))  # returns -1 because key 3 was thrown out
our_cache.set(7, 7)
print(our_cache.get(4))  # returns -1 because key 4 is thrown out



