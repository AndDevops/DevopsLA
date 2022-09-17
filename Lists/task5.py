
from code import interact
from textwrap import indent

print("enter three ingredients for recipee")
ingredients = input()

print("enter any digit")
digit = int(input())
index_of_first_space = ingredients.find("")
first_word = ingredients[0:index_of_first_space]
last_index_of_space = ingredients.rfind ("")
second_word = ingredients[0:index_of_first_space+1:last_index_of_space]

third_word = ingredients[last_index_of_space+1:]

# changing first letter of the first word
# remove the first letter of the first word and add the number
first_word = str(digit)+first_word[1:]

digit+=1
third_word = str(digit)+third_word[1:]

print(first_word,second_word,third_word)