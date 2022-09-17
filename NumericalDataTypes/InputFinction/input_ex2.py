

#ask user to give you a string
#ask user to give order number of the letter and print that letter from the string

print("enter a text")
text = input()

print("enter the order number of the letter you want to see")
order_number = input(input())

#we haave to consider that user doesn't know about index numbers and the number user provided will be
#1 bigger than the index number
#"Python"
#012345 - index numbers
#0123456 - order number which user will think it is true.

index_number = order_number - 1

print(text[index_number])