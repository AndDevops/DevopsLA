

# String "Snicker"
#-- strip,upper,remove prefix and slice the string with any number of your choice
# TASK - 1
#String"Cookie"
# -- lower, replace, 'o' with 'u', remove suffix e, starts with 'C'

s1 = "Snicker"
print(s1.strip().upper().removeprefix("S")[2:5])

s2 = "Cookie"
print(s2.lower().replace("o","u").removesuffix("e").startswith("C"))