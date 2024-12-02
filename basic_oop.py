# Class - a blueprint for creating objects - custom data type

class Car: # Pascal case - eg. HelloThere
    # Constructor - special method that sets up attributes of a new instance
    # will be called automatically when a new instance is created
    def __init__(self, make, model): # self is passed implicitly by the interpreter
        # create an attribute 'make' can copy the value of the 'make param into it
        self.make = make # dot notation - <object>.<attr/method>
        self.model = model
        # implicitly returns self

    def start(self):
        print(f'{self.make} {self.model} started')

# Main
my_car = Car('Honda', 'Civic') # create a new instance of Car
# my_car is now an object of class 'Car'
your_car = Car('Toyota', 'Landcruiser')
# print(my_car.__dict__)
# print(your_car)
my_car.start()
your_car.start()