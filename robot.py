import wpilib
import os
from wpilib import TimedRobot, Spark, Encoder, Joystick
from wpilib.drive import DifferentialDrive
from drivetrain import Drivetrain
from drivestraight import driveStraight
class MyRobot(TimedRobot):

    def robotInit(self):
        self.controller = Joystick(0)
        '''This method is called as the robot turns on and is often used to setup the
        joysticks and other presets.'''
        self.drivetrain = Drivetrain()
        self.driveStraight = driveStraight(self.drivetrain)

        pass
    def robotPeriodic(self):
        '''This is called every cycle of the code. In general the code is loop
        through every .02 seconds.'''
        pass
    def autonomousInit(self):
        '''This is called once when the robot enters autonomous mode.'''

        pass
    def autonomousPeriodic(self):
        self.driveStraight.run()
        '''This is called every cycle while the robot is in autonomous.'''
        pass
    def teleopInit(self):
        '''This is called once at the start of Teleop.'''
        pass
    def teleopPeriodic(self):
        #self.drivetrain.drive(0, 1)
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        self.drivetrain.drive(rotate, forward)
        print(f"rotate:{rotate} forward:{forward}")
        '''This is called once every cycle during Teleop'''
        pass
if __name__ == "__main__":
    # If your ROMI isn't at the default address, set that here
    # If your ROMI isn't at the default address, set that here

    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(MyRobot)