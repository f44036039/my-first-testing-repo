_PARK: str = "Park"
_DRIVE: str = "Drive"
_REVERSE: str = "Reverse"

_GEAR_INPUT_DRIVE: str = 'drive'
_GEAR_INPUT_REVERSE: str = 'reverse'
_GEAR_INPUT_PARK: str = 'park'

from base_car import BaseCar
################################################
# Class name: FancyCar class
# Child class for BaseCar
################################################
class FancyCar(BaseCar):
    ####################################################################################
    # Function: inherit attributes and member functions from BaseCar, 
    #           with some attributes multiplied by input arguments
    #           FancyCar has a horn
    # Input: none
    ####################################################################################
    def __init__(self) -> None:
        super().__init__(maxSpeedConst = 2, accelerationConst = 1, brakeEfficiencyConst = 1)
        self.isHornOn = False
    ####################################################################################
    # End of function __init__
    ####################################################################################

    ####################################################################################
    # Function: changes the direction of the car [`drive` or `reverse`]
    #           cars can only change gears if speed is 0
    #           speed of a car going in reverse is still tracked as positive
    # Input: a str, can only be 'park', 'drive' or 'reverse', ignore capitalization
    ####################################################################################
    def gear(self, dir) -> None:
        if type(dir) != str:
            print("Function gear can only accept a string")
            return

        dir = dir.casefold()
        if dir != 'park' and dir != 'drive' and dir != 'reverse':
            print("Function gear can only accept a string 'park', 'drive' or 'reverse' ")
        
        if self.speed != 0:
            print("Gear can only be changed when speed is 0, please check speed")
            return

        if dir == _GEAR_INPUT_DRIVE:
            self.direction = _DRIVE
            
        if dir == _GEAR_INPUT_REVERSE:
            self.direction = _REVERSE
    ####################################################################################
    # End of function gear
    ####################################################################################
                
    ####################################################################################
    # Function: override the inherited function to include the reverse case
    #           total distance is additive no matter the direction 
    #           relative distance to 'home' will change depending on direction
    # Input: a time value for how long to continue driving
    ####################################################################################
    def drive(self, driveTime):
        try:
            if driveTime < 0:
                print("driveTime must be positive")
                return

            if not self.isDrivingOn:
                print("Drive is not enabled, check if engine is on")
                return
           
            if self.direction == _DRIVE:
                self.distance += self.speed * driveTime
                self.home += self.speed * driveTime

            if self.direction == _REVERSE:
                self.distance += driveTime * self.speed
                self.home -= self.speed * driveTime

            if self.direction == _PARK:
                print("Parking mode, use gear first if you want to drive or reverse")

        except TypeError:
            print("function drive can only accept numbers")
    ####################################################################################
    # End of function drive
    ####################################################################################

    ####################################################################################
    # Function: a horn that goes "beep beep"
    #           horn is noisy, so turn it off after "beep beep"
    # Input: none
    ####################################################################################
    def horn(self):
        self.isHornOn = True
        self.isHornOn = False
    ####################################################################################
    # End of function horn
    ####################################################################################

    ####################################################################################
    # Function: override the inherited function to include the reverse case
    #           show current car stats
    # Input: none
    ####################################################################################     
    def stats(self):
        if self.isEngineOn:
            print("engine: On")
        else:
            print("engine: Off")

        if self.isHeadlightOn:
            print("lights: On")
        else:
            print("lights: Off")

        print(f"speed: {self.speed} m/s")
        print(f"odometer: {self.distance}  m")
        if self.home < 0:
            print(f"home: {-self.home} m")
        else:
            print(f"home: {self.home} m")
        
        print(f"direction: {self.direction}")
        print("")
    ####################################################################################
    # End of function stats
    ####################################################################################

################################################
# End of FancyCar class
################################################