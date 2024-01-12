import os

path = "C:\\Users\\alphus\\Desktop\\Py\\test.txt"
#path = "C:\\Users\\alphus\\Desktop\\Py\\folder"

if os.path.exists(path):
    print("That location exits")
    if os.path.isfile(path):
      print("That is a file")
    #if os.path.isdir(path):
       #print("That is a directory")
else:
  print("That location doesn't exist")  