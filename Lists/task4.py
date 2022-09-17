

# 1 Print the first charachter of given song name.
# 2 Print the last charachter of given song name.
# 3 Print the lenght of the given song name/
#4 Print the index number of "k" in this song name.
# 5 Print the characher from an index number of 3.
# 6 Print the song name in upper case.
# 7 Print the song name in lower case.

#1
print("Enter a song name")
song_name = input()
print(song_name[0])
# 2 
print(song_name[-1])
print(song_name[len(song_name)-1])
#3
print(len(song_name))
#4
print(song_name.find("k"))
#5 
print(song_name[3])
#6
print(song_name.upper())
#7
print(song_name.lower)





