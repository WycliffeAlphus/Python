# nested loop = having a loop inside another loop. Inner loop will finish  all its iterations before finishing one iteration of the outer loop

rows = int(input("How many rows? "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")
for i in range(rows):
    for j in range(columns):
        print(symbol,end="") # without using the end="", we will move to the next line, thus it prevents curser from moving to the next line
    print()    
