
s = "Python"
print(s.islower())
# False 
# letters
print(s.lower()) # python
print(s.lower().islower())
# True because the lower method makes all letters in lower case
s.upper() # Using methods in string will not effect the original
# value of the string.
print(s.isupper())
# False

# Ask user to enter their name in uppercase
# If they didn't enter in upper cases print false

print("Enter your first name in upper cases")
first_name = input()

print(first_name.isupper())
