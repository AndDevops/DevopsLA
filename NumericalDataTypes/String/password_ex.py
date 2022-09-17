

#ask user to enter a password
#if the password doesn't have any uppercase or doesn't have any lower
#case print False, otherwise True.
#Password should have upper case and should have lower case
print("enter a password with upper and lower case letter")
#"password" will be equal to its lower case version
password = input()

is_there_upper = password != password.lower()

#"PASSWORD" wil be iqual to its upper case version
#if the password id not iqual to its upper case version

is_there_lower = password != password.upper();

is_valid_pass = is_there_lower and is_there_upper
print("Your password id valid", is_valid_pass)

