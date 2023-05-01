from drivetrain import Drivetrain
class GyroTurn:
    def __init__(self, drivetrain: Drivetrain, goal):# want to specify that drivetrain is Drivetrain so that it is possible to call drivetain anything
        self.drivetrain = drivetrain()
        self.targetYaw = goal
        self.kp = 1/25
        pass#gas
    def run(self):
        currentYaw = self.drivetrain.getGyroYaw()
        degreesLeft = currentYaw-self.targetYaw #this may have to be reversed
        if abs(degreesLeft) < .5:
            self.drivetrain(0,0)
            return#to sender
        power = self.kp * degreesLeft
        power = max(-.5,min(.5, power))# cap power to .5 and -.5
        print(f"current reading: {currentYaw} power: {power}")
        self.drivetrain(power, 0)
        pass#gas