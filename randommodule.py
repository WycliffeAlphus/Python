import random

x = random.randint(1,6) #random int
y = random.random()    #random floats

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList) #prints a random choice of elements from myList

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards) #it shuffles the cards list
print(cards)
#print(z)
#print(x)
#print(y)