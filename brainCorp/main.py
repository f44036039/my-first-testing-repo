from fast_car import FastCar
from slow_car import SlowCar
from fancy_car import FancyCar

if __name__ == "__main__":

    fastCar = FastCar()
    slowCar = SlowCar()
    fancyCar = FancyCar()

    fastCar.on()
    slowCar.on()
    fancyCar.on()

    fastCar.lights()
    fancyCar.lights()

    fastCar.gas(11)
    slowCar.gas(11)
    fancyCar.gear('drive')
    fancyCar.gas(11)

    fastCar.drive(30)
    slowCar.drive(30)
    fancyCar.drive(30)

    fancyCar.brake(5)
    fancyCar.drive(3)

    slowCar.brake(6)

    fancyCar.fullStop()
    fancyCar.gear('reverse')
    fancyCar.gas(20)
    fancyCar.drive(30)

    slowCar.fullStop()
    slowCar.off()

    fancyCar.lightsOff()

    fastCar.drive(30)
    fastCar.gas(20)
    fastCar.drive(60)

    fastCar.stats()
    slowCar.stats()
    fancyCar.stats()

    fancyCar.horn()
    fancyCar.horn()
    
    slowCar.on()
    slowCar.lights()
    slowCar.gas(4)
    slowCar.drive(2000)
    
    slowCar.stats()
