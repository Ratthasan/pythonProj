'''Create a python class called DriveBot. Within this class, create instance variables for motor_speed, sensor_range, and direction. All of these should be initialized to 0 by default. After setting up the class, create an object from the class called robot_1. Set the motor_speed to 5, the direction to 90, and the sensor_range to 10. Use the provided print statements to check your work!

Hint
Remember that in order to create instance variables inside a class, they need to be within a constructor. For this problem, you can use a constructor with no parameters like so: def __init__(self):. Inside of the constructor, you can then define instance variables: self.motor_speed = 0'''


class DriveBot:
    
    def __init__(self):
        motor_speed = 0
        sensor_range = 0
        direction = 0
        
        
test_bot = DriveBot()
test_bot.motor_speed = 30
test_bot.direction  = 90
test_bot.sensor_range = 25
    

    
    
