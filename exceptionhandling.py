#exception = events  detected during executation that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e: # as e also helps display the exception that occured
    print(e)
    print("You can't divide by zero!")  
except ValueError as e:
    print(e)
    print("Enter only numbers please")      
except Exception:
    print("something went wrong :(")
else:
    print(result)  #executes when there is no exception
finally:
    print("This will always execute")    

