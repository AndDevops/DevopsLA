



#    0123456789
s = "Techtorial"

print(s[4:7])

print(s[4]+s[7])

#ask user the enter a string which lenght is odd and longer than 3
#and print the middle three letters from the string

#"Chicago" - ica
#"seven" - eve

print("enter a string which lenght is odd and longer than 3 letters")
text = input()
#firsr I have to find middle index
middle_index = len(text) //2  #int(len(text)/2)

print(text[middle_index-1:middle_index+2])


#ask user the enter a string which lenght is even and longer than 4
#and print the middle 4 letters from the string

#techtorial - htor
#leyboard - yboa

print("user the enter a string which lenght is even
and longer than 4")
text1 = input()

middle_index = int(len(text1)/2)
print(text1[middle_index-2:middle_index+2])







