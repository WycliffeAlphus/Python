# keyword arguments = arguments preced by an indetifier when we pass them to a function. The order of the arguments doesn't matter, 
#unlike positional arguments Python knows the names of the arguments that our function receives

def hello(first,middle, last):
    print("Hello "+first+" "+middle+" "+last)
#hello("Wycliffe","Alphus","Code") #positional, thus the order matters, changing them also changes the order
hello(last="code",middle="Alphus", first="Wycliffe") #keyword arguments, preceded with an identifier, when passed to a function, the order do not matter   
