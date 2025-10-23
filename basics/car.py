from enum import Enum

class CarStatus(Enum):
    NOTMOVING = "STILL"
    MOVING = "MOVING"



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, inc):
        self.speed += inc

    def display(self):
        print(f"{self.brand} {self.model} is running at {self.speed}")

    def get_status(self):
        if self.speed == 0:
            return CarStatus.NOTMOVING
        return CarStatus.MOVING
    
