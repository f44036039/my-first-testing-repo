from attr import attrs, attrib

@attrs
class BaseCar():
    aveMaxSpeed = 50
    aveAcceleration = 5
    aveBrakeEfficency = -10

    maxSpeedConst = attrib(type = int, default = 1,converter=int)
    # self.accelerationConst = accelerationConst
    accelerationConst = attrib(type = int, default = 1)
    # self.brakeEfficiencyConst = brakeEfficiencyConst
    brakeEfficiencyConst = attrib(type = int, default = 1)

    def multiply(self):
        print(self.aveMaxSpeed * self.maxSpeedConst)

if __name__ == '__main__':
    car_1 = BaseCar()
    BaseCar.multiply()
    # print(type(car_1.maxSpeedConst))