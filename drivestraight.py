import os
from wpilib import TimedRobot, Spark, Encoder, Joystick
from wpilib.drive import DifferentialDrive
from drivetrain import Drivetrain
class driveStraight():
    def __init__(self, Drivetrain, distance):
        self.controller = Joystick(0)
        self.drivetrain = Drivetrain
        self.leftEncoder = Encoder(4, 5)
        self.rightEncoder = Encoder(6, 7)
       # 0.00015271630954950385
        self.leftEncoder.setDistancePerPulse(0.015271630954950385)
        self.rightEncoder.setDistancePerPulse(0.015271630954950385)
        self.speed = 1
        self.drivetrain.drive(0, self.speed)
        self.distance = distance
    def spinUp(self):
        self.drivetrain.drive(0, .75)
    def run(self):
        #self.drivetrain.drive(0,1)
        if(self.leftEncoder.getDistance()>(self.distance*200) or self.rightEncoder.getDistance()>400 ):
            self.drivetrain.drive(0, 0)
            return

        leftRate = self.leftEncoder.getDistance()
        rightRate = self.rightEncoder.getDistance()
        rateDiff = rightRate-leftRate #get the difference in the distances run
        rateDiff = rateDiff /6
        if rateDiff > .3:#cap the difference so the ROMI does not osilate out of control
            rateDiff = .3
        if rateDiff < -.3:
            rateDiff = -.3

        print(f"left rate: {leftRate} right rate: {rightRate} diff: {rateDiff}")
        self.drivetrain.drive(rateDiff,self.speed/1.5)#turn by the post processed differnces
        pass