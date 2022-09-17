
# User want to deposit his money in to his bank account
# he already has $200 in his account
# He has three different paychecks (400, 600, $350)
# He can only deposit one paycheck at a time
# After he deposit all the money in the account
# He bought a phoe for $599, and headphone for $299
# Create a python prigram to calculate his final money in the account.
# Use  input function to get all the values

from concurrent.futures.process import _python_exit


bank_acct = 200

print("Please enter the first paycheck amount you want to deposit")

first_deposit = int(input())

bank_acct+= first_deposit  # this is exactly same
as doing bank_acct = bank_acct + first_deposit

print("Please enter the second paycheck amount you
want to deposit")

second_deposit = int(input())

bank_acct += second_deposit

print("Please enter the third paycheck amount you
want to deposit")

third_deposit = int(input)
print("Please enter the dollar amount of phone you
want to buy")
phone = int(input())

bank_acct-=_python_exit

print("Please enter the dollar amount of head phone
you want to buy")
head_phone = int(input())

bank_acct-= head_phone
print("His final money in the bank account
is",bank_acct)
