# dictionary = A changeable, unorderd collection of unique key: value pairs; Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC', 
            'India': 'New Delhi', 
            'China':'Beijing',
              'Russia':'Moscow'}

capitals.update({'Germany': 'Berlin'}) #used to add a new key, value pair
capitals.update({'USA': 'Las Vegas'}) # change the value of the USA key
capitals.pop('China') # remove the key, value from the dictionary
capitals.clear() #removes everything
#print(capitals['Russia']) # prints the value of the key, Russia, which is Moscow
#print(capitals.get('Germany')) #prevents an error, if a key is not within a dictionary
#print(capitals.keys()) #prints only the keys without the values
#print(capitals.values()) #prints only the values
#print(capitals.items()) #prints the eniter dictionary, that is the keys and the values

for key, value in capitals.items(): 
   print(key, value) #prints entire dictionary


