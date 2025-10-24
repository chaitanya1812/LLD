import Vehicle as v
def test_vehicle():
    print("")

    # "TypeError: Can't instantiate abstract class.."
    # veh = v.Vehicle("new_brand")
    # veh.display_brand()
  
    car = v.Car("Toyota")
    car.start() # abstarct method - custom implemnetation
    car.display_brand() # non abstract method / concrete method of abstract method
    car.display_wheels() # abstract method: using parent implmentation

    trk = v.Truck("Benz")
    trk.start() # abstarct method - custom implemnetation
    trk.display_brand() # non abstract method / concrete method of abstract method
    trk.display_wheels() # abstract method: using custom implmentation in suib class 

    # "TypeError: Can't instantiate abstract class.." because class needs to implement all abstract methods
    # brk = v.Broken("broken") 



