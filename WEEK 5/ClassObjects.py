# Define class
class Car:
    # Attributes(properties)
    def __init__(self,make,model,color):
        self.make = make
        self.model = model
        self.color = color

        # Methods behaivour
    def start(self):
        return f"The {self.color} {self.make} {self.model} starts"
    def stop(self):
        return f"The {self.color} {self.make} {self.model} stops"
    
 #Creating objects (instances) from the Car class
car1 = Car("Toyota","Corolla","red")
car2 = Car("Lamborghini Urus","Lambo22","ping one")

# Interacting with objects
print(car1.start())
print(car1.stop())
print(car2.start())
print(car2.stop())