
list = [2,3,5,True,"s"]

print(len(list)) #5

print(list[4]) #s

print(type(list)) # <class'list'>

print(type(list[3])) #<class'bool'>

print(type(list[4])) #<class 'int'>
print(type(list[2]))#<class'int>

#Slicing the list
print(list[1:4])#<[3,5,True]
print(type(list[1:4]))# <class"list>

print(list[0:3]) #[2,3,5]
print(type(list[0:3]))#<class"list>

print(list[2:])#5,True,'s'
