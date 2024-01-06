# slicing = create a substring by extracting elements from another string
#        indexing[] or slice()
#        [start:stop:step]

#name = "Wycliffe Alphus"

#first_name = name[2]
#first_name = name[0:9] #or first_name = name[:9]
#last_name = name[9:15] #0r last_name = name[9:]
#funky_name = name[0:15:2] # or name[::2]
#reversed_name = name[::-1]

#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)
#step is usually 1 by default, thus optional, but if one wants to print every 2nd character including the 1st, it can be introduced

#slice()

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) #it gives the name of the website, removing the http and .com portion

print(website1[slice])
print(website2[slice])