from base_car import BaseCar
################################################
# Class name: FastCar class
# Child class for BaseCar
################################################
class FastCar(BaseCar):
    ####################################################################################
    # Function name: __init__
    # Input: none
    # Output: inherit attributes and member functions from BaseCar, 
    #         with some attributes multiplied by input arguments
    ####################################################################################
    def __init__(self) -> None:
        super().__init__(maxSpeedConst = 3, accelerationConst= 2, brakeEfficiencyConst= 1)
    ####################################################################################
    # End of function __init__
    ####################################################################################

################################################
# End of FastCar class
################################################
   
 