class BaseCar:
    
    def __init__(self,m=1,a=1,b=1):
        self.maxSpeed=50
        self.acceleration=5
        self.brakeEfficency=-10
        self.maxSpeedConstant = m
        self.accelerationConstant = a
        self.brakeEfficiencyConstant = b

    def getCustomized(self):
        self.maxSpeed = self.maxSpeed * self.maxSpeedConstant
        self.acceleration = self.acceleration * self.accelerationConstant
        self.brakeEfficency = self.brakeEfficency * self.brakeEfficiencyConstant

    def stats(self):
        self.getCustomized()
        print(self.maxSpeed)
        print(self.acceleration)
        print(self.brakeEfficency)
        print("")

class FastCar(BaseCar):
    def __init__(self) -> None:
        super().__init__(3,2,1)

class SlowCar(BaseCar):
    def __init__(self) -> None:
        super().__init__(0.75, 0.75, 2)

class FancyCar(BaseCar):
    def __init__(self) -> None:
        super().__init__(2, 1, 1)
        
#main.py

if __name__ == "__main__":
    car_1 = FastCar()
    car_1.stats()
    
    car_2 = SlowCar()
    car_2.stats()

    car_3 = FancyCar()
    car_3.stats()