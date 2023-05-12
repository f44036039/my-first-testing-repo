from base_car import BaseCar
################################################
# Class name: SlowCar class
# Child class for BaseCar
################################################
class SlowCar(BaseCar):
    ####################################################################################
    # Function name: __init__
    # Input: none
    # Output: inherit attributes and member functions from BaseCar, 
    #         with some attributes multiplied by input arguments
    ####################################################################################
    def __init__(self) -> None:
        super().__init__(maxSpeedConst = 0.75, accelerationConst = 0.75, brakeEfficiencyConst = 2)
    ####################################################################################
    # End of function __init__
    ####################################################################################
    
################################################
# End of SlowCar class
################################################
