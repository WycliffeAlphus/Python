#functions = a block of code which is executed only when it is called.

#def hello(name):
 #   print("hello "+name)
 #   print("Have a nice day!")

def hello(first_name, last_name, age):
    print("Hello "+first_name+ " "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")

#my_name = "Wycliffe"
#hello("Wycliffe")  
#hello("Dude")
#hello(my_name)
hello("Wycliffe", "Alphus", 21)