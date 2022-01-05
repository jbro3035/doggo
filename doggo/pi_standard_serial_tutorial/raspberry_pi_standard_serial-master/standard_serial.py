#
# Jessica's standard serial motor code
#
# RETURNS: Nothing. Motors alternate spinning at full power in timewise direction
#

import time
from serial import Serial
from time import sleep

# Stops both motors
def stopBothMotors(numSec):
    start = time.time()
    diffTime = 0
    while diffTime < numSec:
        current = time.time()
        diffTime = current - start
        roboclaw.write(bytes([0]))          # Shuts down channels 1 and 2 for numSec seconds

# Moves a motor time-wise at full power
def fullForward(motorNum, numSec):
    start = time.time()
    diffTime = 0
    while diffTime < numSec:
        current = time.time()
        diffTime = current - start
        print(diffTime)
        if motorNum == 1:
            roboclaw.write(bytes([127]))      # Channel 1 full forward
        elif motorNum == 2:
            roboclaw.write(bytes([255]))      # Channel 2 full forward
    roboclaw.write(bytes([0]))   

# Stops motor
def stopMotor(motorNum, numSec):
    start = time.time()
    diffTime = 0
    while diffTime < numSec:
        current = time.time()
        diffTime = current - start
        print(diffTime)
        if motorNum == 1:
            roboclaw.write(bytes([64]))     # Channel 1 stop
        else:
            roboclaw.write(bytes([192]))    # Channel 2 stop

# Moves a motor counter-time-wise at full power
def fullReverse(motorNum, numSec):
    start = time.time()
    diffTime = 0
    while diffTime < numSec:
        current = time.time()
        diffTime = current - start
        if motorNum == 1:
            roboclaw.write(bytes([1]))    # Channel 1 full reverse
        else:
            roboclaw.write(bytes([128]))  # Channel 2 full reverse
            
if __name__ == "__main__":

    serial_port = "/dev/ttyS0"
    baudrate = 38400

    roboclaw = Serial(serial_port, baudrate, timeout=1)

    while True:
        #stopBothMotors(100)
        fullForward(1, 3)
        stopMotor(1, 3)
        fullForward(2, 3)
        stopMotor(2, 3)