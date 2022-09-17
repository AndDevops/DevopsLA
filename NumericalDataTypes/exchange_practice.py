
#create a python program to give
#most effficient exchange pissible using only
#coins
#quarter 25 cent
#nickle 5 cent
#dime 10 cents
#penny 1 cent
#$2.34 exchange
#9 quarters
#0 dines
#1 nickle
#4 pennies
#$1.89
#7 quarters 1 dimes 0 nickles and 4 pennies
dollar = 2.96
dollar_amount = 2.96
dollar_amout = dollar * 100
print(type(dollar_amount))
quarter_value = 25
dime_value = 10
nickel_value = 5
penny = 1


count_of_q = dollar_amount // quarter_value
print("We need to give back")

print(count_of_q)

remaining_exchange_after_q = dollar_amount % quarter_value

count_of_d = remaining_exchange_after_q // dime_value
print(count_of_d, "dimes")
remaining_exchange_after_d = remaining_exchange_after_q % dime_value
count_of_nickel = remaining_exchange_after_d // nickel_value
print(count_of_nickel, "nickels")
remaining_exchange_after_nickel = remaining_exchange_after_d % nickel_value
count_of_pennies = remaining_exchange_after_nickel // penny
print(count_of_pennies, "pennies")

count_of_pennies = remaining_exchange_after_nickel// penny
