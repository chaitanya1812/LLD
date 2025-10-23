
import pytest

from car import Car

def test_initial_state():
    car = Car("Toyota", "Corolla")
    assert car.brand == "Toyota"
    assert car.model == "Corolla"
    assert car.speed == 0

def other():
    car = Car("Tesla", "Model_1")
    assert car.brand == "Tesla"
    assert car.model == "Model_1"
    assert car.speed == 0
    car.display()

def test_display(capsys):
    car = Car("Toyota", "Corolla")
    car.accelerate(40)
    car.display()
    captured = capsys.readouterr()
    # print(captured)
    assert captured.out.strip()  == "Toyota Corolla is running at 40"

def test_status():
    car = Car("Toyota", "Corolla")
    car.accelerate(40)
    status = car.get_status()
    print(status.name, status.value)
    car.speed = 0
    status = car.get_status()
    print(status.name, status.value)


if __name__ == "__main__":
    pytest.main()
    # other()







