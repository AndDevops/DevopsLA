
# Ask user to enter a positive integer number
# Check if the given number is within 2 of a multiple of 10.
# If it is within 2 of a nultiple 10 print 
# Your number os within 2 of a multiple 10
# If not print your number didn't match the expected requirement.

# 10 - 20 - 30 - 40 - 50 -- so on
# If the user gives 21 -- your number is within 2 of a multiple 10
# If the user gives 43 -- your number is wihtin a multiple 10
# We need to use remainder operator.

# If the given number remainder with 10 is less than equal to 2
# It means it is withing 2 of a multiple 10
# 11 % 10 -- 1
# 22 % 10 --2
# 30 % 10 --0

# 9 ---  10
# 18 --  
# If the also given number remainder with 10 is bigger or equal to 8
# The given number is within 2 of a multiple 10

 #                     8 9 10 11 12
 #                   38 39 40 41 42

 print ("Enter a positive integer number")
 num = int(input())

 remainder = num % 10
 if remainder<=8 or remainder<=2:
    print("your number didn't natch the expected requirement.")


