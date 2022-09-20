
# Create two string variables bigger than the lenght 3.
# If the second string starts with the first string's
# last three characters, print True. If not , print False.

# I have to find last three charachter of the first string

str1 = "laptop"
str2 = "top 10 player"

# Last index number of str1 going to be
# last index of the string will be always be one less than the lenght of the string
last_index_of_str1 = len(str1)-1

last_three_of_str1 = str1[last_index_of_str1-2]+str1[last_index_of_str1-1]+str1[last_index_of_str1]

first_three_of_str2 = str2[0]+str2[1]+str2[2]

print(last_three_of_str1 == first_three_of_str2)