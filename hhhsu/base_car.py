_AVE_MAX_SPEED: int = 50
_AVE_ACCELERATION: int = 5
_AVE_BRAKE_EFFICIENCY: int = -10

_INIT_HOME: int = 0
_INIT_DISTANCE: int = 0
_INIT_SPEED: int = 0

_PARK: str = "Park"
_DRIVE: str = "Drive"
################################################
# Class name: BaseCar class
# Average Car
# Parent class for FastCar, SlowCar and FancyCar
################################################
class BaseCar:
    ####################################################################################
    # Function: initiate the car with different maxSpeed, acceleration and brakeEfficiency
    # Input: unique car features
    ####################################################################################
    def __init__(self, maxSpeedConst = 1, accelerationConst = 1, brakeEfficiencyConst = 1) -> None:
        self.aveMaxSpeed = _AVE_MAX_SPEED
        self.aveAcceleration = _AVE_ACCELERATION
        self.aveBrakeEfficency = _AVE_BRAKE_EFFICIENCY

        self.maxSpeedConst = maxSpeedConst
        self.accelerationConst = accelerationConst
        self.brakeEfficiencyConst = brakeEfficiencyConst

        self.maxSpeed = self.aveMaxSpeed * self.maxSpeedConst
        self.acceleration = self.aveAcceleration * self.accelerationConst
        self.brakeEfficency = self.aveBrakeEfficency * self.brakeEfficiencyConst

        self.distance = _INIT_DISTANCE
        self.speed = _INIT_SPEED

        self.isGasOn = False
        self.isDrivingOn = False
        self.isBrakingOn = False

        self.isEngineOn = False
        self.isHeadlightOn = False
        self.direction = _PARK
    ####################################################################################
    # End of function __init__
    ####################################################################################
    
    ####################################################################################
    # Function: turns on engine (allows for gas, driving, and braking to take affect)
    #           establishing starting point ('home') on the ILR
    #           if engine is turned off and on, then the home value will be reset to 0
    # Input: none
    ####################################################################################
    def on(self) -> None:
        self.isEngineOn = True
        self.isGasOn = True
        self.isDrivingOn = True
        self.isBrakingOn = True
        
        self.home = _INIT_HOME
    ####################################################################################
    # End of function on
    ####################################################################################
   
    ####################################################################################
    # Function: turns off engine (disallows gas, driving, and braking)
    #           engine cannot turn off while car is still moving (speed must be 0)
    # Input: none
    ####################################################################################
    def off(self) -> None:
        if self.speed != 0:
            print("Engine cannot be turned off when speed is not 0")
            return
            
        self.isEngineOn = False
        self.isGasOn = False
        self.isDrivingOn = False
        self.isBrakingOn = False
        self.direction = _PARK
    ####################################################################################
    # End of function off
    ####################################################################################
   
    ####################################################################################
    # Function: accelerates the car depending on how long the gas pedal is pressed
    #           not affect distance, only affects speed
    #           speed should not exceed maxSpeed
    # Input: a time value for how long the pedal is pressed to accelerate
    ####################################################################################
    def gas(self, pedalTime) -> None:
        try:
            if pedalTime < 0:
                print("pedalTime must be positive")
                return

            if not self.isGasOn:
                print("Gas is not enabled, check if engine is on")
                return
            
            self.speed += self.acceleration * pedalTime
            if self.speed > self.maxSpeed:
                self.speed = self.maxSpeed
        except TypeError:
            print("Function gas can only accept numbers")
    ####################################################################################
    # End of function gas
    ####################################################################################
    
    ####################################################################################
    # Function: continues driving in same direction
    #           no change in acceleration, coasting at a steady speed
    #           average cars can only move forward
    # Input: a time value for how long to continue driving
    ####################################################################################
    def drive(self, driveTime) -> None:
        try:
            if driveTime < 0:
                print("driveTime must be positive")
                return

            if not self.isDrivingOn:
                print("Drive is not enabled, check if engine is on")
                return
            
            if self.speed < 0:
                print("Average car can only move forward")
                return
                
            self.distance += driveTime * self.speed
            self.home += driveTime * self.speed
            self.direction = _DRIVE
        except TypeError:
            print("Function drive can only accept numbers")
    ####################################################################################
    # End of function drive
    ####################################################################################
  
    ####################################################################################
    # Function: slows down the vehicle
    #           not affect distance, only affects speed
    # Input: a time value for how long the pedal is pressed to brake
    ####################################################################################
    def brake(self, brakeTime) -> None:
        try:
            if brakeTime < 0:
                print("brakeTime must be positive")
                return

            if not self.isBrakingOn:
                print("Brake is not enabled, check if engine is on")
                return

            self.speed += self.brakeEfficency * brakeTime
            if self.speed < 0:
                self.speed = 0

        except TypeError:
            print("Function brake can only accept numbers")
    ####################################################################################
    # End of function brake
    ####################################################################################
   
   ####################################################################################
    # Function: bring the car to a full stop
    # Input: None
    ####################################################################################
    def fullStop(self) -> None:
        if not self.isBrakingOn:
            print("Brake is not enabled, check if engine is on")
            return

        brakeTime = round(self.speed / self.acceleration)
        self.brake(brakeTime)
        self.direction = _PARK
    ####################################################################################
    # End of function fullＳtop
    ####################################################################################
  
    ####################################################################################
    # Function: turn on lights despite if the engine is on/off
    # Input: None
    ####################################################################################
    def lights(self) -> None:
        self.isHeadlightOn = True
    ####################################################################################
    # End of function lights
    ####################################################################################
  
    ####################################################################################
    # Function: turn off lights despite if the engine is on/off
    # Input: None
    ####################################################################################
    def lightsOff(self) -> None:
        self.isHeadlightOn = False
    ####################################################################################
    # End of function lightsOff
    ####################################################################################
    
    ####################################################################################
    # Function: show current car stats
    # Input: None
    ####################################################################################
    def stats(self) -> None:
        if self.isEngineOn:
            print("engine: On")
        else:
            print("engine: Off")

        if self.isHeadlightOn:
            print("lights: On")
        else:
            print("lights: Off")

        print(f"speed: {self.speed} m/s")
        print(f"odometer: {self.distance} m")
        print(f"home: {self.home} m")
        print(f"gear: {self.direction}")
        print("")
    ####################################################################################
    # End of function stats
    ####################################################################################
   
################################################
# End of BaseCar class
################################################