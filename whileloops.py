#while loop = statement that will execute it's block of code as long as it's condition remain true. 

#name = ""

#while len(name) == 0:
#    name = input("Enter your name: ")
 #   print("Hello "+name)

name = None
while not name:
    name = input("Enter your name: ")
    print("Hello "+name)
