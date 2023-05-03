from drivetrain import Drivetrain
from wpimath.controller import PIDController
from autoroutine import AutoRoutine
class GyroTurn(AutoRoutine):
    def __init__(self, drivetrain: Drivetrain, goal):# want to specify that drivetrain is Drivetrain so that it is possible to call drivetain anything
        self.drivetrain = drivetrain()
        self.targetYaw = goal
        self.pid_controller = PIDController(1/120,1/1000,0) # takes in P, I and D
        self.pid_controller.setSetpoint(self.goal)
        self.pid_controller.setTolerance(3)
        self.pid_controller.setIntegratorRange(-.2,.2)
        #self.kp = 1/80
        #self.ki = -1/800
        self.turnDeadzone = .5
        self.maxTurnSpeed = .5
        #self.total_error = 0
        #self.maxTotalError = 1/self.ki
        pass#gas
    def run(self):
        currentYaw = self.drivetrain.getGyroYaw()
        degreesLeft = currentYaw-self.targetYaw #this may have to be reversed
        power = self.pid_controller.calculate(currentYaw)
        #self.total_error += degreesLeft
        #self.total_error = max(-self.maxTotalError,min(self.maxTotalError, self.total_error)) # cap the total error
        if self.pid_controller.atSetpoint():#stop turning if in deadzone (really double the set deadzone, because of abs, so /2)
            self.drivetrain(0,0)
            return#to sender
        #power = self.pid_controller.calculate(currentYaw)
        power = max(-self.maxTurnSpeed,min(self.maxTurnSpeed, power))# cap power to maxTurnSpeed
        print(f"{currentYaw=} {power=}")
        self.drivetrain(power, 0)
        pass#gas