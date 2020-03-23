"""
List is collection of items in a particular order
a list is created by placing all the items (elements) inside a square bracket [ ], separated by commas
"""
"""
List Common Methods
 append() - Add an element to the end of the list
 extend() - Add all elements of a list to the another list
 insert() - Insert an item at the defined index
 remove() - Removes an item from the list by it's name
 pop() - Removes and returns an element at the given index
 clear() - Removes all items from the list
 index() - Returns the index of the first matched item
 count() - Returns the count of number of items passed as an argument
 sort() - Sort items in a list in ascending order
 reverse() - Reverse the order of items in the list
 copy() - Returns a shallow copy of the list
"""

user_list = ['bob', 'alice', 'eve', 'devil', 'david', 'joseph']

# print(user_list)
# print(sorted(user_list))

""" CRUD(Cread,Read,Update,Delete) Functionality in List """
# Create a list item
user_list.append('append')
user_list.insert(1, 'Broken Heart')

""" Read list item by specific item index and all at a time """
# print(user_list[1]) # as index start from 0 alice will be the output
# print(user_list)
# print(user_list[:3]) # read first 3 items of the list

""" Updating  list item """
user_list[1] = 'update Broken'
print(user_list)

""" Delete List item """
del user_list[0]  # bob going to be delete
print(user_list)

user_list.remove('update Broken')

print("after removing user broken update: " +str(user_list))

# Now we are going to delete item using pop,so that we can track the item which has been deleted
track = user_list.pop(0)
print(track + " has been deleted")
print("Now the list of items are: " + str(user_list))
# print("Total items that are david:" + str(user_list.count('david')))
print("Total item on the list is:"+str(len(user_list)))