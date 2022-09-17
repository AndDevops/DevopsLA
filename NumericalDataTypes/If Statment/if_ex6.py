
# In the factory we need to create a program that can
# find if we can do the shipment and if we can do the shipment 
# it will tell use how many small package we should ship.
# first we need to get total kg of the shipment,
# to reach this total kg of shipment we can use small and big packages.
#Every big package is 5kg and evey small packeges is 1kg
# We have limited namount of small and big packages.
# Ask user how many big and how many small package they have.
# Ask user what is the total goal kg of the shipment.
# Print whether they can ship, if they can ship print gow many small packages they need.
# Assume big packages is used before small packages.

# count of small packege = 4 -- 4kg
# count of big packege = 1 -- 5kg
# goal is to ship 9kg
# I can ship and I need to use 4 small package

# 5 small packege -- I need to use 3 small package
# 4 big package -- how many big package I need to use -- 2
# I need to ship 13kg
# I can ship and I need to use 3 small package

# 3 small package -- I need to use 4 small package to complete but since I don't
# have 4 small package I cannot ship
# 3 big package -- I can use max 2 big package
# I need ship 14kg
# I cannot ship

print("Enter the kg we need to ship")
goal_ship_ = int(input())

print("Enter amount of small packages you have")
count_of_small = int(input())

print("Enter amount of big packages you have")
count_of_big = int(input())

# I have to start from big packages to reach goal kg
# How can I find how many big packages I need to reach to goal?

needed_big_packages = goal_ship // 5

# If I dont't have enough big packages can I do the shipment- No

# 9 small packages
# 1 big package
# I need to ship 14kg
if needed_big_packages<=count_of_big:
    #How many small package I need
    needed_small_packages = goal_ship_%5
    if needed_small_packages <= count_of_small:
        print (f"I can do the shipment and I need {needed_small_packages} amount of small package")
    else:
        print("I cannot do the shipment")
else:
    # How many kg can I reach with the big boxes I have and then the rest of the amount I will 
    # try to complete with using small packages
    kg_i_have = count_of_big * 5;
    left_goal = goal_ship - kg_i_have
    # Left goal divided by 1 will give amount of small package I need
    if left_goal<=count_of_small:
        print("I cannot do the shipment and I need {left_goal} amount of small boxes")
    else :
        print("I cannot do the shipment.")
