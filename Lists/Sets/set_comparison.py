
# The are some mehtods we can compare two set with each other.

s1 = {1,7,9,3}

s2 = {2,7,9,5}
# differentce method will get the elements present
#in set, that is not present in the other set.

print(s1.difference(s2))#{1,3}

print(s2.difference(s1))#{2,5}

# what do you think the return type of difference method?
print(s2.difference(s1))#<class'set'>

#intersection
s1 = {1,7,9,3}

s2 = {2,7,9,5}
#intersection method will return elements that are present in the both sets.
print(s1.intersection(s2)) #{9,7}
print(type(s1.intersection(s2)))#class'set'>

#issubset()
# It check given set is present in the other set or not.
set = {1,2,3,4,5}
set2 = {2,3,4}
# Since all elements of the set2 is in the set set2 is subset of the set.

print(set2.issubset(set)) # True
print(set.issubset(set2))#false

# issuperset()
# If the set has all the elements of other set, it is called superset of the set2
print(set.issuperset(set2)) #True
print(set2.issuperset(set))#False

#intersection_update
#It will remove all the elements that are not present in the other set
#intersection_update doesn't have a return type.
s1 = {1,2,3}

s2 = {2,3}
s1.intersection_update(s2)
print(s1)

s2.intersection_update(s1)
print(s2)


# difference_update,

s1 = {1,2,3,}
s2 = {2,3}
# difference update mehtod doesn't have a return type.

s1.difference_update(s2)
print(s1)

s3 = {1,2,3}
s2.difference_update(s3)

print(s2)#empty set
























