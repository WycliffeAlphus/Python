#nested function calls = function calls inside another function call
#innermost function calls are resolved first
#returned value is used as argument for the next function

#num = input("Enter a whole postove number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))
