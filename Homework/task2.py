
print("Enter any string with spaces")
s1 = input()


s1 = s1.replace(" ","")

is_Lenght_Odd = len(s1) % 2!=0

print(is_Lenght_Odd)