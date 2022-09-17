
need = ["pencil","eraser","notebook"]

need2 = ["computer","mouse","keyboar","camera"]

need.extend(need2)
print(need)

# What happens if you extend list with string
str = "Techorial"
str.upper()
list = [1,2,3,4,5]
print(str) # "Techorial"

list.extend(str)
print(list) #[]
#[1,2,3,4,5,'T','e','c','h','t','o','r','i','a','l']
# extend method only works with iterable objects.

# list.extend(1234) # it will create an error