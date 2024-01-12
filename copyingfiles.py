#copyfile() = copies contents of a file
#copy() = copyfile() + persmision mode + destination can be a directory
#copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

#shutil.copyfile('test1.txt','C:\\Users\\alphus\\desktop\\copy.txt') #src, destination are the arguments
shutil.copyfile('test1.txt', 'copy.txt') #puts it in the current workspace
