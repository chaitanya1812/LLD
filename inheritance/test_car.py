import car as c
def test_car():
    print()
    ec = c.ElectricCar()
    ec.make = "Tesla"
    ec.model = "Model Y"

    ec.charge_battery()
    ec.start_engine()
    ec.stop_engine()
    ec.display_make_model()

    fc = c.GasCar("Toyota","Corolla")
    fc.fill_tank()
    fc.fuel_percentage = 50
    fc.display_fuel()
    fc.start_engine()
    fc.stop_engine()
    fc.display_make_model()


    # We can use the parent calss as normal class if needed
    car = c.Car("new", "model")
    car.start_engine()
    car.stop_engine()
    car.display_make_model()

