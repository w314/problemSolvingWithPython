# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler, not_found_handler = None):
        self.root = RouteTrieNode(handler)
        self.not_found_handler = not_found_handler

        
    def insert(self, path_list, handler):
   
        # set root to node
        node = self.root
        
        # traverse through tree, add nodes as needed
        for path in path_list:
            if path not in node.children:
                node.children[path] = RouteTrieNode()
            node = node.children[path]
        
        # when whole path is added, add handler
        node.handler = handler

        
    def find(self, path_list):
#       
        # set node to root
        node = self.root
        
        # traverse through tree to find path or return None if not existent
        for path in path_list:
            if path in node.children:
                node = node.children[path]
            else:
                return None
            
        # return handler
        return node.handler

    
class RouteTrieNode:
    def __init__(self, handler = None):
        self.children = {}
        self.handler = handler
        
        
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_handler = None):
        self.trie = RouteTrie(handler, not_found_handler) 

    def add_handler(self, path, handler):
        # split path
        split_path = self.split_path(path)
        
        # call node's insert method with path array and handler
        self.trie.insert(split_path, handler)

        
    def lookup(self, path):
        # split path
        split_path = self.split_path(path)
        
        # call nodes' find method to find handler
        handler = self.trie.find(split_path)
        
        # return handler if there is one, not_found_handler if handler is 'None'
        return handler if handler else self.trie.not_found_handler


    def split_path(self, path):
        
        # split path and remove first ''
        split_path = path.split('/')[1:]
        
        # if there was a trailing '/' now there is a trailing ''
        # remove that to handle pathes ending with or without '/' in the same way
        if len(split_path) > 0 and split_path[-1] == '':
            split_path = split_path[:-1]
        
        # return split_path array
        return split_path
        
        
print('TESTING PROBLEM 7 (HTTPRouter Using a Trie)')

print('\nTest Case 1')
print('testing for path ""')
router = Router("root handler", "not found handler")
path = ''
print('path to check for handler: ', path)
handler = router.lookup(path)
print('handler returned: ', handler)
# returns 'root handler'

print('\nTest Case 2')
print('testing for path "/"')
router = Router("root handler", "not found handler")
path = '/'
print('path to check for handler: ', path)
handler = router.lookup(path)
print('handler returned: ', handler)
# returns 'root handler'

print('\nTest Case 3')
print('testing add_handler function')
router = Router("root handler", "not found handler")
path = '/home/about'
handler = 'about handler'
router.add_handler(path, handler)
print('path to add: ', path)
print('handler to add: ', handler)
print('check handler just added:')
path = '/home/about'
print('path to check for handler: ', path)
handler = router.lookup(path)
print('handler returned: ', handler)
# returns 'about handler'

print('\nTest Case 4')
print('testing finding path ending without "/" with handler ')
router = Router("root handler", "not found handler")
path = '/home/about'
handler = 'about handler'
router.add_handler(path, handler)
print('router content:')
print('path added: ', path)
print('handler added to path above: ', handler)
print('looking for handler:')
path = '/home/about'
print('path to check for handler: ', path)
handler = router.lookup(path)
print('handler returned: ', handler)
# returns 'about handler'

print('\nTest Case 5')
print('testing finding path ending with "/" with handler ')
router = Router("root handler", "not found handler")
path = '/home/about'
handler = 'about handler'
router.add_handler(path, handler)
print('router content:')
print('path added: ', path)
print('handler added to path above: ', handler)
print('looking for handler:')
path = '/home/about/'
print('path to check for handler: ', path)
handler = router.lookup(path)
print('handler returned: ', handler)
# returns 'about handler'

print('\nTest Case 6')
print('testing finding path with no handler')
router = Router("root handler", "not found handler")
path = '/home/about'
handler = 'about handler'
router.add_handler(path, handler)
print('router content:')
print('path added: ', path)
print('handler added to path above: ', handler)
print('looking for handler:')
path = '/home'
print('path to check for handler: ', path)
handler = router.lookup(path)
print('handler returned: ', handler)
# returns 'not found handler'

print('\nTest Case 7')
print('testing finding non existent path')
router = Router("root handler", "not found handler")
path = '/home/about'
handler = 'about handler'
router.add_handler(path, handler)
print('router content:')
print('path added: ', path)
print('handler added to path above: ', handler)
print('looking for handler:')
path = '/find_this'
print('path to check for handler: ', path)
handler = router.lookup(path)
print('handler returned: ', handler)
# returns 'not found handler'     
