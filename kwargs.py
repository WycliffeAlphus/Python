# **kwargs = parameter that packs all arguments into a dictionary, 
# useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs): #accept varying amounts of keyword arguments
    #print("Hello "+ kwargs['first'] + " " +kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
#hello(first="Wycliffe", middle="Alphus", last = "Code")    #the arguments vary to what is printed in the function
hello(title="Mr.", first="Wycliffe", middle="Alphus", last = "Code")        

## kwargs can be anything, what is important are the tow asterix. kwargs just mean key word argument

