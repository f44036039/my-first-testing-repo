# One Car, Two Car, Fast Car, Slow Car

__Project Description__

This project simulates 3 types of car ruuning on a straight line. fastCar, slowCar and fancyCar share the same feature, with different parameters. fancyCar also has some unique features, as described later.

__Parameters for different types of car__
| Feature          | FastCar | SlowCar | FancyCar |
| ---------------- | :-----: | :-----: | :------: |
| Max Speed        |   3x    |  .75x   |    2x    |
| Acceleration     |   2x    |  .75x   |    1x    |
| Brake Efficiency |   1x    |   2x    |    1x    |

__Package__

This project use the package `pytest`, to test the code.

__Installation__

Download and extract the hhhsu.zip file to a directory, then run the main.py file. Files in the '/tests' folder cannot be run directly, please put them one level higher, to the same directory as base_car.py, fast_car.py, slow_car.py and fancy_car.py before running them.

__Common API__

1. on()
   - turns on engine (allows for gas, driving, and braking to take affect)
   - establishing starting point ('home') on the road
2. off()
   - turns off engine (disallows gas, driving, and braking)
   - engine cannot turn off while car is still moving (speed must be 0)
3. gas(pedalTime)
   - adds gas to the engine, accelerates the car
   - Accelerates the car depending on how long the gas pedal is pressed (in secs)
   - pedalTime is a number represents time value for how long the pedal is pressed to accelerate
   - will not affect distance, only affects speed
4. drive(driveTime)
   - continues driving in same direction
   - driveTime a number represents time value for how long to continue driving (in secs)
   - no change in acceleration (These cars should assume there is no natural deceleration, if the car is driving, then it is coasting at a steady speed)
   - fastCar and slowCar can only move forward
   - fancyCar can only be driven after gear('drive') or gear('reverse') is called
5. brake(brakeTime)
   - slows down the vehicle
   - brakeTime is a number represents time value for how long the pedal is pressed to brake (in secs)
   - will not affect distance, only affects speed
6. lights()
   - can turn on the lights despite the engine is on/off
7. lightsOff()
   - can turn off the lights despite the engine is on/off
8. stats()
   - show current car stats:
     - engine on/off
     - headlights on/off
     - current speed
     - odometer:
       - distance traveled in trip
     - home:
       - distance from 'home'
     - current gear (direction car is moving)
       - park: when speed is 0
       - drive: moving forward
       - reverse: moving backward

__Unique API for fancyCar__

1. gear(dir)
   - changes the direction of the car
   - should be used before calling drive(driveTime) on fancyCar
   - dir is a string, either 'drive', 'reverse' or 'park', UPPER CASE or lower case doesn't matter

2. horn()
   - enable the horn that goes "beep beep"
   - will be turned off immediately since it's noisy
---