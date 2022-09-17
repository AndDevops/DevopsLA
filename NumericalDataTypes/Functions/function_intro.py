# We want to reuse the piece of code or algorithm,
# WE create functions and reuse them.
# syntax of creating a function is-> def nethod_name.

def print_name():
    print(Techtorial.)

# Methods only work when they get called.
print_name()

# Let's create a method for greeting.
# It will take user's name as argument and will print,
# Hello User'sName
def print_greeting(name):
    print(f"Hello{name}")

print("Enter your name")
user_name = input()
print_greeting(user_name)

# Let's create a method for greeting.
# It will take user's name as argument and will print,
# Hello User'sName
def get_greeting(name):
    return f"Hello{name}"
# Methods includes what is indented but it is recommended to leave
#2 lines of space after the last line of 



















#create a method to find sum of given two integer.
# Give means the method will take it as parameter.
# Add an if statment in this method so it will print error occured
def sum(num1,num2):
    addition = num1 + num2
s            =


# Methods will always stop when the code reaches the return statment.

def sum2(*nums):
    sum = 0
    for element in nums:
        sum +=element

        return sum

print(sum2(1,5,6,8,9))