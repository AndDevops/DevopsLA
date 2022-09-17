
# Prime number
# prinme numbers can only be divided by 1 and itself.
# for example:
# 3 can only be divided by 1 and 3
# 7 can only be divided by 1 and 7
# 11
# 13
#19
# 17
# 23 is prime
# you should ask user to give a number
# Find out if the given number is prime number or not prime number.

# The given should not be divided by any other number than 1 and itself
# I have to check all the numbers that is smaller than given number to see
# if they can divide  the given number.

# 18 is it possible divide 18 with the number bigger than 18

print("Enter a number")
num = int(input())

# I have to start checking from possible divisors
# What is the smaller number that you can divide the non prime numbers other than 1?
#2
# 12 % 2 == 0
# Using break statement we can stop the loop regardless of the condition.
# How can I print when the number is a prime?

# To undertand if the number is a prime we should check all possible divisors 
# and see none-of them can divide the number
# in the code below where do you top checking all possible divisors?
# You stop checking all possible divisors when the loop ends
# When if statment in the loop never gets executed it means given number is prime
is_prime = True
possible_divisor = 2
while possible_divisor < num:
    if num % possible_divisor == 0:
        # When this if statment gets executed it neans given number is not prime
        # whenever this if  statments gets executed I don't have to check rest of the 
        # possible divisors to understand if it is a prime
        # How can I tell the code given number is not prime?
        print("It is not a prime")
        is_prime = False
        # if you understand the number is not prime no need to continue to rest  of 
        # of the loop
        break 
    possible_divisor+=1
if is_prime:
    print("this is a prime number")
else:
    print("This is not a prime number")