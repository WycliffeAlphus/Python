#scope = the region that a variable is recognized
# a varibale is only available inside the region it is created
# a global and locally scoped versions of a variable can be created

name = "Wycliffe" #global variable (available inside and outside the function) but wihtin the current molule
def display_name():
    #name = "Alphus" #local variable(available only inside this function)
    print(name)
display_name()   
print(name)

#Python starts by using the local variable, if present, if not it moves to the enclocing varibale, global, then builtin (LEGB)