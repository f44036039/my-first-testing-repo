
class BaseCar:
    
    def __init__(self, maxSpeedConst = 1, accelerationConst = 1, brakeEfficiencyConst = 1) -> None:
        self.aveMaxSpeed = 50
        self.aveAcceleration = 5
        self.aveBrakeEfficency = -10

        self.maxSpeedConst = maxSpeedConst
        self.accelerationConst = accelerationConst
        self.brakeEfficiencyConst = brakeEfficiencyConst

        self.maxSpeed = self.aveMaxSpeed * self.maxSpeedConst
        self.acceleration = self.aveAcceleration * self.accelerationConst
        self.brakeEfficency = self.aveBrakeEfficency * self.brakeEfficiencyConst

        self.home = 0
        self.distance = 0
        self.speed = 0

        self.isGasOn = False
        self.isDrivingOn = False
        self.isBrakingOn = False

        self.isEngineOn = False
        self.isHeadlightsOn = False
        self.direction = "Park"


    def on(self):
        self.isEngineOn = True
        self.isGasOn = True
        self.isDrivingOn = True
        self.isBrakingOn = True
        
        self.home = 0

    def off(self):
        if self.speed != 0:
            return
            
        self.isEngineOn = False
        self.isGasOn = False
        self.isDrivingOn = False
        self.isBrakingOn = False
        self.direction = "Park"
            
    def gas(self, pedalTime):
        if not self.isGasOn:
            return

        self.speed += self.acceleration * pedalTime
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed

    def drive(self, driveTime):
        if not self.isDrivingOn:
            return
        
        if self.speed < 0:
            return

        self.distance += driveTime * self.speed
        self.home += driveTime * self.speed
        self.direction = "Drive"

    def brake(self, brakeTime):
        if not self.isBrakingOn:
            return

        self.speed += self.brakeEfficency * brakeTime
        if self.speed < 0:
            self.speed = 0


    def lights(self):
        self.isHeadlightsOn = True

    def lightsOff(self):
        self.isHeadlightsOn = False

    def stats(self):
        if self.isEngineOn:
            print("engine: On")
        else:
            print("engine: Off")

        if self.isHeadlightsOn:
            print("lights: On")
        else:
            print("lights: Off")

        print("speed: " + str(self.speed) + " m/s")
        print("odometer: " + str(self.distance) + " m")
        print("home: " + str(self.home) + "m")
        print("gear: " + str(self.direction))
        print("")


class FastCar(BaseCar):

    def __init__(self) -> None:
        super().__init__(maxSpeedConst = 3, accelerationConst= 2, brakeEfficiencyConst= 1)
        
        
class SlowCar(BaseCar):
    
    def __init__(self) -> None:
        super().__init__(maxSpeedConst = 0.75, accelerationConst = 0.75, brakeEfficiencyConst = 2)
        

class FancyCar(BaseCar):
    
    def __init__(self) -> None:
        super().__init__(maxSpeedConst = 2, accelerationConst = 1, brakeEfficiencyConst = 1)
        self.isHornOn = False

    def gear(self, dir):
        if self.speed != 0:
            return

        if dir == 'drive':
            self.direction = 'Drive'
            
        if dir == 'reverse':
            self.direction = 'Reverse'
                        

    def drive(self, driveTime):
        if not self.isDrivingOn:
            return

        if self.direction == 'Drive':
            self.distance += self.speed * driveTime
            self.home += self.speed * driveTime

        if self.direction == 'Reverse':
            self.distance += driveTime * self.speed
            self.home -= self.speed * driveTime

    def horn(self):
        self.isHornOn = True

        
    def stats(self):
        if self.home < 0:
            self.home = - self.home

        return super().stats()
            


if __name__ == "__main__":

    car_1 = FastCar()
    car_1.on()
    car_1.gas(1)
    car_1.drive(10)
    car_1.brake(3)
    car_1.off()
    car_1.stats()

    car_2 = FancyCar()
    car_2.lights()
    car_2.on()
    car_2.gear('reverse')
    car_2.gas(1)
    car_2.drive(10)
    car_2.stats()
