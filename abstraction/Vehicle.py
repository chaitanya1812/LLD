from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        # abstract method needs to implement in the subclasses.
        pass

    @abstractmethod
    def display_wheels(self):
        # abstract method needs to implement in the subclasses.
        # else: for default behaviour/to trigger this implmentation call super().method_name()
        print(f"Abstract class : Wheels : 4")
    
    # concrete method - full implmentation here in this abstract class.
    def display_brand(self):
        print(f"Abstract Class : this is {self.brand}")

# subclass needs to implement all abstract methods 
class Car(Vehicle):
    # using same constructor as parent class
    def __init__(self, brand):
        super().__init__(brand)
    
    # implement abstract method:
    def start(self):
        print("car is starting...")
    

    # instead of implementing abstract method / call parent method
    def display_wheels(self):
        super().display_wheels()


# subclass needs to implement all abstract methods 
class Truck(Vehicle):
    # using same constructor as parent class
    def __init__(self, brand):
        super().__init__(brand)
    
    # implement abstract method:
    def start(self):
        print("Truck is starting...")

    # implement abstract method:
    def display_wheels(self):
        return print(f"Wheels : 8")

    # this is a concrete method present in parent class / implementation here overrides parent implementaiton
    def display_brand(self):
        print(f"this is overriden implementation display_brand: {self.brand}")

# Can't instantiate class without implentations of all abstract methods
class Broken(Vehicle):
    # using same constructor as parent class
    def __init__(self, brand):
        super().__init__(brand)
    
    # implement abstract method:
    def start(self):
        print("Broken is starting...")

    # don't implement abstract method -> causes "TypeError: Can't instantiate abstract class.."
    # def display_wheels(self):
    #     return print(f"Wheels : 8")

    # this is a concrete method present in parent class / implementation here overrides parent implementaiton
    def display_brand(self):
        print(f"this is overriden implementation display_brand: {self.brand}")
