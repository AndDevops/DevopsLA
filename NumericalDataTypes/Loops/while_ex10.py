
# Ask user to enter a string
# If the given string contains any duplicate letter
# print string has duplicated letter
# otherwise print string consists of unique letters.

print("Enter a string")
str =input()

# we should check for each letter, if there is duplication
is_unique = True
index = 0
while index < len(str):
    if str.count(str[index])>1:
        # it means there is duplicated letter
        is_unique = False
        break
    index+=1

if is_unique==True:
    print("Strint consists of unique letters")
else:
    print("Strint has duplicated letters")


