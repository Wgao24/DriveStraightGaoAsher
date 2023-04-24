import os
from wpilib import TimedRobot, Spark, Encoder, Joystick
from wpilib.drive import DifferentialDrive
from drivetrain import Drivetrain
class driveStraight():
    def __init__(self, Drivetrain):
        self.controller = Joystick(0)
        self.drivetrain = Drivetrain
        self.leftEncoder = Encoder(4, 5)
        self.rightEncoder = Encoder(6, 7)
        self.leftEncoder.setDistancePerPulse(0.01828668723656)
        self.rightEncoder.setDistancePerPulse(0.01828668723656)
        self.speed = 1
        self.drivetrain.drive(0, self.speed)

    def spinUp(self):
        self.drivetrain.drive(0, .75)
    def run(self):
        #self.drivetrain.drive(0,1)
        #if(self.leftEncoder.getDistance()>4 or self.rightEncoder.getDistance()>4 ):
         #   self.drivetrain.drive(0, 0)
         #   pass#gas

        #leftRate = self.leftEncoder.getRate()
        #rightRate = self.rightEncoder.getRate()
        leftRate = self.leftEncoder.getDistance()
        rightRate = self.rightEncoder.getDistance()
        rateDiff = rightRate-leftRate
        #rateDiff = rateDiff/50
        #rateDiff = rateDiff**3
        #rateDiff = rateDiff * 5
        rateDiff = rateDiff /6
        if rateDiff > .3:

            rateDiff = .3
        if rateDiff < -.3:
            rateDiff = -.3

        print(f"left rate: {leftRate} right rate: {rightRate} diff: {rateDiff}")
        self.drivetrain.drive(rateDiff,self.speed/1.5)#Goes right when the thing is positive?
        pass