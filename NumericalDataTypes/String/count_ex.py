
# Ask user to give two different string values
# If the first string containes the second string
# return True, if not return False.

print("Enter first string")
s1 = input()

print("Enter second string")
s2 = input()
# If the firsr string doesn't contain the second string
# count of second string in the  first one should be 0

count_of_second = s1.count(s2)
is_contain = bool(count_of_second)
print(is_contain)