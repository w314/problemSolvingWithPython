# Function finds all files under a directory (and all directories beneath it) that end with ".c"

import os




def find_files(suffix, path):
   
    # check if path is valid
    if not os.path.isdir(path):
        # if path is a file with the required suffix return the file
        if os.path.isfile(path) and path.endswith(suffix):
            return [path]
        # otherwise return empty list
        else:
            print('Invalid path')
            return []
    
    output = list()
    
    def find_file_rec(path):
        
        # get contents of directory
        contents = os.listdir(path)

        # process content
        for content in contents:
            content_path  = os.path.join(path, content)
            # if it's a file
            if os.path.isfile(content_path):
                # check suffix and add to output if it's correct
                if content_path.endswith(suffix):
                    output.append(content_path)
            # if directory call find_file_rec with this directory's path
            else:
                find_file_rec(content_path)

    find_file_rec(path)
    return output



# TESTING find_files
print('\nTESTING find_files')

print('\nTest Case 1')
print('testing invalid path given as parameter')
suffix = '.c'
path = 'alma'
print(find_files(suffix, path))
# prints 'Invalid path', returns []

print('\nTest Case 2')
print('testing with file with correct suffix given as path')
suffix = '.c'
path = '..\\testdir\\t1.c'
print(find_files(suffix, path))
# returns file in list


print('\nTest Case 3')
print('testing with file with incorrect suffix given as path')
suffix = '.alma'
path = '..\\testdir\\t1.c'
print(find_files(suffix, path))
# prints 'Invalid path', returns []

print('\nTest Case 4')
print('testing when no file is found with the given suffix')
suffix = '.alma'
path = '..\\testdir'
print(find_files(suffix, path))
# returns []

print('\nTest Case 5')
print('testing when files with suffix are found')
suffix = '.c'
path = '..\\testdir'
print(find_files(suffix, path))
# returns all files with suffix even in subdirectories