



print("Enter any text with three words")
three_words = input()
last_index_of_firstWord = three_words.find(" ")-1

last_index_of_secondWord = three_words.rfind(" ")-1

last_index_of_lastWord = len(three_words)-1

print(last_index_of_firstWord+last_index_of_secondWord+last_index_of_lastWord)
