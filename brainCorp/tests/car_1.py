from fast_car import FastCar
from slow_car import SlowCar
from fancy_car import FancyCar

if __name__ == "__main__":
    
    car_1 = FastCar()
    car_1.on()
    car_1.gas(1)
    car_1.drive(10)
    car_1.brake(3)
    car_1.off()
    car_1.stats()