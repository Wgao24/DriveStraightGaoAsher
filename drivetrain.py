import os

import wpilib
from wpilib import TimedRobot, Spark, Encoder
from wpilib.drive import DifferentialDrive
import romi # for gyro
class Drivetrain:
    def __init__(self):

        self.left_motor = Spark(0)
        self.right_motor = Spark(1)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)
        self.gyro = romi.RomiGyro()#init gyro
        self.accelerometer = wpilib.BuiltInAccelerometer()# init accelerometer
    def getGyroYaw(self):
        """returns the yaw of the robot in degrees"""
        return self.gyro.getAngleZ()
        pass#gas
    def resetGyro(self):
        """resets angles to all be zero"""#this allows people to see what the fuction does as a preview when they use it in another class
        self.gyro.reset()
        pass#gas
    def drive(self, rotate, forward):
        """takes in rotate, and forward and does the thing
        """
        self.drivetrain.arcadeDrive(rotate,forward)

