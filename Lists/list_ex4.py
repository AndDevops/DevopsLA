
# Create a program that will ask user ten full name
# After you get 10 full name create email version of given 10
# name and store it inside list and print.
# enter full name
# John Wick
# enter full name
# Max White

# ["johnwick@gmail.com", "maxwhite@gmail.com",....]

full_names =[]
emails = []

for i in range(10): #by using range will don't need to repeate operation 10 times
    print("Enter a full name")
    f_name = input()
    f_name = f_name.replace(",").lower()+"gmail.com"
    emails.append(f_name)# append add elements in the end of the list.

print(full_names)
print(emails)
