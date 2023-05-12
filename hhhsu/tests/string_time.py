from fast_car import FastCar
from slow_car import SlowCar
from fancy_car import FancyCar
import pytest

def string_fast():
  print('First we try on FastCar')
  string_fast_car = FastCar()
  string_fast_car.on()

  string_fast_car.gas('3')
  assert string_fast_car.speed == 0, "fail on function gas, speed should be 0"
  assert string_fast_car.distance == 0, "fail on function gas, distance should be 0"

  string_fast_car.drive('-6')
  assert string_fast_car.speed == 0, "fail on function drive, speed should be 0"
  assert string_fast_car.distance == 0, "fail on function drive, distance should be 0"

  string_fast_car.brake('5')
  assert string_fast_car.speed == 0, "fail on function brake, speed should be 0"
  assert string_fast_car.distance == 0, "fail on function brake, distance should be 0"
  
  print("All tests on negative input in fastCar is passed!")

def string_fancy():
  print("Now test on FancyCar")
  string_fancy_car = FancyCar()
  string_fancy_car.on()

  string_fancy_car.gear('wow')
  assert string_fancy_car.speed == 0, "fail on function gear, speed should be 0"
  assert string_fancy_car.distance == 0, "fail on function gear, distance should be 0"
  assert string_fancy_car.direction == 'Park', "fail on function gear, distance should be 0"
  
  string_fancy_car.gas('3')
  assert string_fancy_car.speed == 0, "fail on function gas, speed should be 0"
  assert string_fancy_car.distance == 0, "fail on function gas, distance should be 0"

  string_fancy_car.drive('9')
  assert string_fancy_car.speed == 0, "fail on function drive, speed should be 0"
  assert string_fancy_car.distance == 0, "fail on function drive, distance should be 0"
  
  string_fancy_car.brake('-7')
  assert string_fancy_car.speed == 0, "fail on function brake, speed should be 0"
  assert string_fancy_car.distance == 0, "fail on function brake, distance should be 0"

  print("All tests on negative input in fancyCar is passed!")

if __name__ == "__main__":

  string_fast()
  string_fancy()
  
