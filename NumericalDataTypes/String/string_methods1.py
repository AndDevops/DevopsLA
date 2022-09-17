

s = "Python"

print(s.upper()) # - PYTHON

print(s) #  - Python
#Since the string is immutable, it will not change its value unless it is reasigned.

s = "Python"
print(s.lower())

#method chaining - as long the method you use in the string
#you can use other string methods
print(s.lower.upper()) # s will be printed in all upper case since it is the last method
print (s.upper.lower()) #s will be printed in all lower case since it is the last method

