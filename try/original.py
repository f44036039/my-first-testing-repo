
class BaseCar:
    
    def __init__(self) -> None:
        self.maxSpeed = 50
        self.acceleration = 5
        self.brakeEfficency = -10
        

    def getCustomized(self, maxSpeedConstant, accelerationConstant, brakeEfficiencyConstant):
        self.maxSpeed = self.maxSpeed * maxSpeedConstant
        self.acceleration = self.acceleration * accelerationConstant
        self.brakeEfficency = self.brakeEfficency * brakeEfficiencyConstant

    def on():
        pass

    def off():
        pass

    def gas():
        pass

    def drive():
        pass

    def brake():
        pass

    def headlights():
        pass

    def checkDashBoard():
        pass

    def stats(self):
        print(self.maxSpeed)
        print(self.acceleration)
        print(self.brakeEfficency)
        print("")

class FastCar(BaseCar):
    def __init__(self) -> None:
        super().__init__()
        maxSpeedConstant = 3
        accelerationConstant = 2
        brakeEfficiencyConstant = 1
        self.getCustomized(maxSpeedConstant,accelerationConstant,brakeEfficiencyConstant)


class SlowCar(BaseCar):
    def __init__(self) -> None:
        super().__init__()
        maxSpeedConstant = 0.75
        accelerationConstant = 0.75
        brakeEfficiencyConstant = 2
        self.getCustomized(maxSpeedConstant,accelerationConstant,brakeEfficiencyConstant)


class FancyCar(BaseCar):
    def __init__(self) -> None:
        super().__init__()
        maxSpeedConstant = 2
        accelerationConstant = 1
        brakeEfficiencyConstant = 1
        self.getCustomized(maxSpeedConstant,accelerationConstant,brakeEfficiencyConstant)


if __name__ == "__main__":

    car_1 = FastCar()
    car_1.stats()

    car_2 = SlowCar()
    car_2.stats()

    car_3 = FancyCar()
    car_3.stats()