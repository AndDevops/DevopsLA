
total_value = 2.8# this is a dollar amout
value_in_cents = 100+total_value # value of the dollar amout in cents

value_of_q = .25
value_of_d = .1
value_of_n = .05
value_of_p = .01

number_of_q = value_in_cents // value_of_q

remaining_balance = value_in_cents % value_of_q

number_of_dimes = remaining_balance //value_of_d

remaining_balance = remaining_balance % value_of_d

number_of_n = remaining_balance //value_of_n

remaining_balance = remaining_balance % value_of_n

number_of_pennies = remaining_balance // value_of_p

print(f"""You will get {number_of_q}amout quarters, {number_of_dimes}amout of dimes,{number_of_n}
amout of nickels and lastly you will get {number_of_pennies}amout of pennies.""")