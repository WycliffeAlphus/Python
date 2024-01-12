import os
import shutil # helps deletes folders with files

#path = "text.txt"
#path ="empty_folder"
path = "folder"


try:
    #os.remove('text1.txt')
    #os.rmdir(path) # this deletes folders that are empty
    shutil.rmtree(path) #Note that it deletes directory(folder) and all files within it.
except FileNotFoundError:
    print('File not found')    
except PermissionError:
    print("You do not have permission to delete that!")    
except OSError:
    print("You cannot delete that using that function")
except:
    print(path+ " was deleted")    