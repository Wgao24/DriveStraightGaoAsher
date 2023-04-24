import os
from wpilib import TimedRobot, Spark, Encoder
from wpilib.drive import DifferentialDrive

class Drivetrain:
    def __init__(self):
        self.left_motor = Spark(0)
        self.right_motor = Spark(1)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)

    def drive(self, forward, rotate):
        self.drivetrain.arcadeDrive(forward,rotate)

