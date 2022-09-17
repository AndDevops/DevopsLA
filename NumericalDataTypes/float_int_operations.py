# Every math operation between float and int data typw
#will result in float data type

floatnum = 3.0
intnum = 5

print("type of floatnum is", type(floatnum))
print("typw of intnum is", type(intnum))

addition = floatnum + intnum
print("addition of float and int is", type(addition))

subtraction = intnum - floatnum
print("subtraction between int and float is",type(subtraction))

multiplication = floatnum * intnum
print("multiplication between int data type and float is", type(multiplication))

division = intnum / floatnum
print ("division between int and float data type is", type(division))

remainder = floatnum % intnum
print("remainder between float and int data type is", type(remainder))

remainder2 = intnum % floatnum
print("remainder between flot and int data type is",type(remainder2))

#There id only one way to get int which is using //
int_division = floatnum // intnum
print("integer symbol division result between float and integer is", type(int_division))

square_of_float = floatnum * floatnum
print(type(square_of_float))
