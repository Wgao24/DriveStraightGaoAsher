from typing import Protocol

class AutoRoutine(Protocol): #this is not a class, it is a protocol
    def run(self):
        ...

    def reset(self):
        ...