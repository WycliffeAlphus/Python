# str,format() = optional method that gives users more control when displaying output

#animal = "cow"
#item = "moon"

#print("The " +animal +" jumped over the "+item)
#print("The {} jumped over the {}".format(animal,item)) #or print("The {} jumped over the {}".format("cow","moon")) 
#print("The {0} jumped over the {1}".format(animal,item)) #positional argument; using indexing
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument

#text = "The {} jumped over the {}"
#print(text.format(animal,item)) #this formats the text variable by calling the format method

# The curly braces are known as format fields and fuction as placeholders for a value of a varibale and work in order, the first format field
#inserts the first value at the location, the next value listed within the format method is  inserted in the the next format field.

#name = "Wycliffe"

#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}. Nice to meet you".format(name)) #adding a padding to the right of the name
#print("Hello, my name is {:<10}. Nice to meet you".format(name)) #this is left aligning, though not visible since it is the default
#print("Hello, my name is {:>10}. Nice to meet you".format(name)) #this right aligns the value
#print("Hello, my name is {:^10}. Nice to meet you".format(name)) #this center aligns

#number = 3.14159
number = 1000

#print("The number pi is {:.2f}".format(number)) #display only the first two digits after the decimil in the format field, the f is for floating point numbers
print("The number pi is {:,}".format(number)) #adds a comma to all one thousands spaces
print("The number pi is {:b}".format(number)) #display binary of the number
print("The number pi is {:o}".format(number)) #displayed as octal number
print("The number pi is {:X}".format(number)) #displayed as hexadecimal
print("The number pi is {:E}".format(number)) #scientific notation
