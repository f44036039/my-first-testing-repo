from fast_car import FastCar
from slow_car import SlowCar
from fancy_car import FancyCar

if __name__ == "__main__":

    car_2 = FancyCar()
    car_2.lights()
    car_2.on()
    car_2.gear('reverse')
    car_2.gas(1)
    car_2.drive(10)
    car_2.stats()