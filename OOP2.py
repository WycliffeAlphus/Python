class Car:

    def __init__(self,make,model,year,color):    
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self): #self refers to the object using the method
        print("This "+self.model+ " is driving")
    def stop(self):
        print("This "+self.model+ " is stopped")    