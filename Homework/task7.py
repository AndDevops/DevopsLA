

#1. Ask the user to enter a random word using input function.
#2. Then ask the user to input the number of letters that word consists of.
#3. Lastly ask the user for a letter that they want to learn its index. 
#4. Your code should print True if the user entered a right number of 
# 5 letters in the word. Print False if the wrong number is entered.
#6.Your code should print the index of the entered letter, if the word doesn’t
# contain the letter then the code should print -1.
#7.Please look at the example output below to understand how your code
# should work.

print("Enter a string")
s1 = input()

print("Enter the number of letters in the string")
user_guess = int(input())

print("Enter any letter that you want to learn its index")
letter = input()

is_guess_correct = len(s1) == user_guess
print(is_guess_correct)

print(s1.find(letter))