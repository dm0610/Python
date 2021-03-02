nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend

# Add the name to the empty set

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()
name = input("List names of you friends: ")
while name:
    user_friends.add(name)
    name = input("add name: ")
shared_friends = nearby_people.intersection(user_friends)
print(f"shared_friends: {shared_friends}")
