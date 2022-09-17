
# prefix - will remove from the beggining of the string
# suffix - will remove it from the end of the string.

s = "Hello Python"
# If you want to remove Python from this string you can use
# remove suffix method
print(s.removesuffix("Python"))

print(s.removeprefix("Hello"))
# This method is case sensitive

# From the given website string,
#print only the domain name of the website

web_site = "Techtorial.com"
damain_name = web_site.removeprefix("www").removesuffix(".com")

print("domain_name")

str = "hello word"
print(str.removeprefix('el'))
# 1- "hlo world"
print(str.removeprefix("el"))

str2 = "Encapsulation is good for data hiding"
print("Result of the suffix",str2.removesuffix("gni"))
print("Result of strip",str2.strip("gni"))
# "Encapsulation is good for data hiding"
# "Encapsilation is good for data hid"
# Encapsulation is good for data hidi"
