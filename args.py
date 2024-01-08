# *args = parameter that will pack all arguments into a tuple, 
#useful so that a function can accepts a varying amount of arguments

def add(*args): #the args can be named anything, the important thing is the asterix, the packs everything into a tuple
    sum = 0
    args = list(args)          #to change an argument in the tuple after passing them you have to cast it into a list, since tuples cannot be changed unlike lists
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

