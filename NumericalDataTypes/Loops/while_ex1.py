
# Ask uder to give you a string
# From that string print index numbers of all the e's
#
print ("Enter a text")
str = input()

# We can access string elements using their index.
index = 0

# Index number is always smaller than lenght of the string.
# "Exemple"
# 0123456 Index numbers
#   7  Lenght of the string
lenght_of_str = len(str)

while index < lenght_of_str:
    # I want to access the element with index str[index]
    if str[index] == "e":
        print(f"Index number of e is {index}")
    index +=1
