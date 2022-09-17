
num1, num2 = 4,6

print(num1 ==num2)# False

is_numbers_equal = num1 == num2

print(is_numbers_equal)
print(type(is_numbers_equal))

print(is_numbers_equal==(num1 == num2)) #True

print(num1!=4) # False because value of the variable num1 is 4


comparison = num1 !=num2
print(comparison) # It is True because num1 and num2 have different values

b3 = num1 > num2

print(b3) # False

num1 += 2
# On the line above num1 will take the value 6 and since 6 is biggger equals to num2
# the following line will out put True
print(num1>=num2) # True

print(True!=True) # False
print(False==False) # True

a = "Text1"
b = "Text1"
print(a==b) # True because the value of the a and b is the same

b = "text"
print(a ==b) # False because values are not the same anymore
