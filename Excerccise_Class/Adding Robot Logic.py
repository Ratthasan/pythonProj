'''In the DriveBot class, add a method called control_bot which accepts parameters: new_speed and new_direction. These should replace the associated instance variables. Create another method called adjust_sensor which accepts a parameter called new_sensor_range which replaces the sensor_range instance variable. Afterwards, use these methods to rotate the robot 180 degrees at 10 miles per hour with a sensor range of 20 feet. Use the provided print statements to check your code!

Hint
Remember that the format for creating methods in a class looks like this: def method_name(self, variable_1, variable_2): and we can modify instance variables like so: self.instance_variable_name = variable_1.'''


class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
        
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 10
robot_1.direction = 180
robot_1.sensor_range = 20

