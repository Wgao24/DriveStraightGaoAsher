from wpimath.controller import PIDController
from wpilib import Encoder, Joystick
from autoroutine import AutoRoutine

class driveUpRamp(AutoRoutine):
    def __init__(self, Drivetrain, distance):
        self.controller = Joystick(0)
        self.drivetrain = Drivetrain
        self.leftEncoder = Encoder(4, 5)
        self.rightEncoder = Encoder(6, 7)
        # 0.00015271630954950385
        self.leftEncoder.setDistancePerPulse(0.015271630954950385)
        self.rightEncoder.setDistancePerPulse(0.015271630954950385)
        self.pid_controller = PIDController(1 / 120, 1 / 1000, 0)  # takes in P, I and D
        self.pid_controller.setSetpoint(0)  # drive straight
        self.pid_controller.setTolerance(.05)
        self.pid_controller.setIntegratorRange(-.2, .2)
        self.maxTurnSpeed = .5
        self.speed = .75
        # self.drivetrain.drive(0, self.speed)
        self.distance = distance
        self.onRamp = False

    def spinUp(self):
        self.drivetrain.drive(0, .75)

    def run(self):
        Pitch = self.drivetrain.getGyroPitch()
        # self.drivetrain.drive(0,1)
        # maybe add a thing that stops rotating when hit the setpoint.
        if (Pitch > 10):
            self.onRamp = True
        elif (self.onRamp == True): #ramp stop logic
            self.drivetrain.drive(0, 0)
            return
        leftRate = self.leftEncoder.getDistance()
        rightRate = self.rightEncoder.getDistance()
        rateDiff = rightRate - leftRate  # get the difference in the distances run
        turnPower = self.pid_controller.calculate(rateDiff)
        #      if rateDiff > .3:#cap the difference so the ROMI does not osilate out of control
        #          rateDiff = .3
        #      if rateDiff < -.3:
        #          rateDiff = -.3
        turnPower = max(-self.maxTurnSpeed, min(self.maxTurnSpeed, turnPower))

        print(f"left rate: {leftRate} right rate: {rightRate} {turnPower=}")
        self.drivetrain.drive(turnPower, self.speed)  # turn by the post processed differnces
        pass