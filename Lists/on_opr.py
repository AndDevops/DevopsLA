
# using in operator we can specified value is in the list or not.
# We can also use in operator for strings as well.

list = [1,2,3,4,5]

if 2 in list:
    print("2 is in the list")

if 11 in list:
    print("11 is in the list.") # This line will not work because
#11 is not in the list.

# not in operator will check if the specified value is not in the iterable objects.

if 6 not in list:
    print(6,"is not in the list")
    # 11 is not in  the list.

# not  operator will check if the specified value is not in the iterable objects.
if 6 not in list:
    print(6,"is not in the list")

# Ask user to enter a random digit
# check if the digit is present in our list or not.
# if user enters present element print you won a prize,
# if not, print mayby, next time.
print("Enter a random digit")
digit = int(input())

if digit in list:
    print("You have won a prize")
elif digit not in list:
    print("Mayby,next time")

# in operator can be used for every iterable object.
