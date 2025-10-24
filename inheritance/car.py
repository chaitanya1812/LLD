class Car:
    def __init__(self, make=None, model=None):
        self.make = make 
        self.model = model

    def start_engine(self):
        print("Base Class: Engine Started...")

    def stop_engine(self):
        print("Base Class: Engine Stopped...")
    
    def display_make_model(self):
        print("Base Class: ", self.make, self.model)


class ElectricCar(Car):
    def __init__(self, make=None, model=None):
        super().__init__(make, model)
        self.battery_percentage = 0.0 # extended variable in child class

    # extended method in child class
    def charge_battery(self):
        print("Battery Charging...")

    # extended method in child class
    # accessing variables from super class and child class
    def display_battery(self):
        print(f"Battery : {self.battery_percentage} for {self.make} {self.model}")

    

class GasCar(Car):
    def __init__(self, make=None, model=None):
        super().__init__(make, model)
        self.fuel_percentage = 0.0 # extended variable in child class

    # extended method in child class
    def fill_tank(self):
        print("Filling gas tank...")

    # extended method in child class
    # accessing variables from super class and child class
    def display_fuel(self):
        print(f"Fuel : {self.fuel_percentage} for {self.make} {self.model}")

    # overriden method in child class
    def display_make_model(self):
        print("Child Class: ", self.make, self.model)

