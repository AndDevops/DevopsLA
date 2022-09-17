
#Write the program to get the string value from the specified position.
#First, ask the user to enter one String value. Then ask the user to the
#enter starting number and ending number. After that, print the value
#between the given starting and ending numbers. (Note: since the user
#does not know the python, the user starts counting from 1, and the
#ending number will be included)

print("Please enter a string value")
s1 = input()

print("Please enter starting number")
starting_num = int(input())
print("Please enter ending number")
ending_num = starting_num -1

print(s1[starting_num:ending_num])
