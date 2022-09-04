'''Create a class variable called all_disabled which is set to False. Next, create two more class variables called latitude and longitude. Set both of those variables to equal -999999. A third robot has been created below the first two robots. Set the latitude of all of the robots to -50.0 at once. Additionally, set the longitude of the robots to 50.0 and set all_disabled to True. You should be able to set those values using three lines of code.

Hint
You can create class variables directly in the class without placing them in the constructor. Also, to change the value of the class variable within all objects of the class, access the class variable directly from the class. Here is an example: DriveBot.class_variable = 5.'''

class DriveBot:
    all_disabled = False
    latitude = -99999
    longtitude = -99999
    

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

DriveBot.latitude = 50.0
DriveBot.longtitude = -50.0
DriveBot.all_disabled = True 



#print(robot_1.latitude)
#print(robot_1.longtitude)
#print(robot_1.all_disabled)


