
# We use two methods to remove elements from the set.
# discard() method and remove()method.

#remove(valueOfTheObject)

set = {3,5,7,9}

# i want to remove the number from the set.
print(set)

# When the element needs to be removed does not exist in the set
#it will throw an error.
#set.remove(7)

#discard(valueOfTheObject)method

set.discard(3)
print(3)

#when the element needs to be removed does not exist in the set 
#it will not throw an error and it won't anything.
set.discard(3)