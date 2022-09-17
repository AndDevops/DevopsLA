
# getting ticket for speed violatiion
#   in state of IN, speed limit on HighWays is 70
# in other states, speed limit on HighWays is 55
#-if driver esceeds speed limit forup to 10% of the limit in each state,
# we will give Warning in that state
# state of IN warningmeans--- print---"Yellow warning"

# other state warning mean-- print---"Citation"
#- if driver exceeds speed limit more than 10% of the limit in each state,
# we wil give Ticket in that state
# state ofIN ticket means--print--"$150 and 5 points"
# other state warning mean-- print--"you are driving safe!"

speed_lemit_IN_others =70,55

print("What state are you in at the moment?")
speed_of_driver = int(input())

print("What state are you in at the moment?")
state_in = inpt()

# If the condition below is True driver is in IN
#If the driverr is not in Indiana the condition below will be False
is_in_ IN = state_in_ == "IN"
#print(npt is_IN)

ten_percent_up_IN = speed_limit_IN + speed_limit_IN*10/100

ten_percent_up_others = speed_limit_others + speed_limit_others*10/100

if is_in_IN and speed_of_driver<=speed_limit_IN:
    print("You are driving safe!")
elif is_in_IN and speed_of_driver>speed_limit_IN and speed_of_driver<=ten_percent_up_IN:
    print("Yellow Warning")
elif is_in_IN and speed_of_driver>ten_percent_up_IN:
    print("$150 and 5 points")
elif is_in_IN and speed_of_driver<=speed_lemit_IN_others:
    print("You are driving safe!")
elif not is_in_IN and speed_of_driver>speed_limit_others and speed_of_driver=ten_percent_up_others:
    print("citation")
elif not is_in_IN and speed_of_driver>ten_percent_up_others:
    print("$100")









# - If speed is same as speed limit, - "You are driving safe"

speed_limit_IN, speed_limit_others = 70,55

print("Ehat speed are you travelling at the moment")
speed_of_driver = int(input())

print("What state are you in at the moment?")
state_in = input()

#If the condition below is True driver is in IN
#If the driver is not in IN this condition will be False
is_in_IN = state_in =="IN"
ten_percent_up_IN = speed_limit_IN_ + speed_limit_IN*10/100
if is_in_IN and speed_of_driver<=speed_limit_IN:
    print("You are driving safe")
elif id_in_IN and speed_limit_IN and speed_of_driver<=ten_percent_up_IN:
    print("Yellow Warning")
elif is_in_IN and speed_of_driver>ten_percent_up_IN:
    print("150 and 5 points")
elif not is_in_IN and speed_of_driver<speed_limit_others and speed_of_driver<=ten_percent_up_others:
    print("citation")
elif not is_in_IN and speed_of_driver>ten_percent_up_others:
    print("$100")


