from fast_car import FastCar
from slow_car import SlowCar
from fancy_car import FancyCar
import pytest

def negative_fast():
  print('First we try on FastCar')
  negative_fast_car = FastCar()
  negative_fast_car.on()

  negative_fast_car.gas(-3)
  assert negative_fast_car.speed == 0, "fail on function gas, speed should be 0"
  assert negative_fast_car.distance == 0, "fail on function gas, distance should be 0"

  negative_fast_car.drive(-6)
  assert negative_fast_car.speed == 0, "fail on function drive, speed should be 0"
  assert negative_fast_car.distance == 0, "fail on function drive, distance should be 0"

  negative_fast_car.brake(-8)
  assert negative_fast_car.speed == 0, "fail on function brake, speed should be 0"
  assert negative_fast_car.distance == 0, "fail on function brake, distance should be 0"
  
  print("All tests on negative input in fastCar is passed!")

def negative_fancy():
  print("Now test on FancyCar")
  negative_fancy_car = FancyCar()
  negative_fancy_car.on()

  negative_fancy_car.gear(-1)
  assert negative_fancy_car.speed == 0, "fail on function gear, speed should be 0"
  assert negative_fancy_car.distance == 0, "fail on function gear, distance should be 0"
  assert negative_fancy_car.direction == 'Park', "fail on function gear, distance should be 0"
  
  negative_fancy_car.gas(-2)
  assert negative_fancy_car.speed == 0, "fail on function gas, speed should be 0"
  assert negative_fancy_car.distance == 0, "fail on function gas, distance should be 0"

  negative_fancy_car.drive(-3)
  assert negative_fancy_car.speed == 0, "fail on function drive, speed should be 0"
  assert negative_fancy_car.distance == 0, "fail on function drive, distance should be 0"
  
  negative_fancy_car.brake(-5)
  assert negative_fancy_car.speed == 0, "fail on function brake, speed should be 0"
  assert negative_fancy_car.distance == 0, "fail on function brake, distance should be 0"

  print("All tests on negative input in fancyCar is passed!")

if __name__ == "__main__":

  negative_fast()
  negative_fancy()
  
