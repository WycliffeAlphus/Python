try:
    with open('test.txt') as file: #with open closes files automatically after opening them
        print(file.read())
# print(file.closed)    # if the file is closed it prints true, if open it prints false
    
except FileNotFoundError:
    print("That file was not found :()")
    