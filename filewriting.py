#text ="Yoooooo\nThis is some text\nHave a good one!"
text = "\nHave a nice day!"
#with open('test1.txt','w') as file: #writing a file, change mode to w; default is r for read
with open('test1.txt', 'a') as file:  #appending a file, change the mode to a
    file.write(text)