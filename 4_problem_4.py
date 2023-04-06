# provided by udacity
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


# function returns if user is part of a group or not
def is_user_in_group(user, group):
    
    in_group = False
    
    # check users in group
    group_users = group.get_users()
    for group_user in group_users:
        if group_user == user:
            return True
    
    # check subgroups
    sub_groups = group.get_groups()
    for sub_group in sub_groups:
        in_group =  is_user_in_group(user, sub_group)
    
    return in_group



# TESTING is_user_in_group
print('\nTESTING is_user_in_group')

# setting up groups and users for testing
# create groups
food = Group('food')
colors = Group('colors')
fruits = Group('fruits')
vegetables = Group('vegetables')
salads = Group('salads')

# create subgroups
food.add_group(fruits)
food.add_group(vegetables)
vegetables.add_group(salads)

# create users
food.add_user('pancake')
colors.add_user('green')
vegetables.add_user('pumpkin')
salads.add_user('kale')
salads.add_user('spinach')


# Test Case 1
print('\nTest Case 1')
print('testing non-existent user')
user = 'dog'
group = food
print(is_user_in_group(user, group))
# returns False

# Test Case 2
print('\nTest Case 2')
print('testing a direct user of a group')
user = 'pancake'
group = food
print(is_user_in_group(user, group))
# returns True

# Test Case 3
print('\nTest Case 3')
print('testing a user of a subgroup')
user = 'kale'
group = food
print(is_user_in_group(user, group))
# returns True

# Test Case 4
print('\nTest Case 4')
print('testing a valid user not part of the group passed as the parameter')
user = 'kale'
group = fruits
print(is_user_in_group(user, group))
# returns False

