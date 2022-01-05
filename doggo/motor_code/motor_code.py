#!/usr/bin/env python
#
# Jessica's Python code 
#
# Runs motors with Raspberry Pi. Will be used in doggo project. 
#
# Returns nothing, powers motors on robot. Placeholder for what code actually does

# Import required modules
import time
import RPi.GPIO as GPIO

# Helper function to set up pins 
def setUpPins(allPins):
    for pin in allPins:
        GPIO.setup(pin, GPIO.OUT)
    
# Drive motor clock-wise
def driveMotorCW(pinNum1,pinNum2):
    GPIO.output(pinNum1, GPIO.HIGH) # Set AIN1
    GPIO.output(pinNum2, GPIO.LOW)  # Set AIN2
    
# Drive motor counter-clock-wise
def driveMotorCCW(pinNum1, pinNum2):
    GPIO.output(pinNum1, GPIO.LOW)  # Set AIN1
    GPIO.output(pinNum2, GPIO.HIGH) # Set AIN2
    
# Drives multiple motors, either clock-wise or counter-clock-wise    
def driveMultMotors(motorPinNums, direction):
    for pin in range(len(motorPinNums)):
        if pin.find('1') != -1:
            if direction == 'cw':
                driveMotorCW(pin, pin + 1)
            else
                driveMotorCCW(pin, pin + 1)
    
# Set motor speed
def setMotorSpeed(allPins):
    for pin in allPins:
        if pin.find('PWM') != -1:
            GPIO.output(pin, GPIO.HIGH)
    
# Disable standby
def disableStandby(pinNum):
    GPIO.output(pinNum, GPIO.HIGH) # STBY
    
# Wait sec number of seconds
def wait(sec):
    time.sleep(sec);
    
# Reset the GPIO pins by setting them to low 
def resetPins(pins):
    for pin in pins:
        GPIO.output(pin, GPIO.LOW) 

def main():
    AIN1 = 12
    AIN2 = 11
    PWMA = 7
    STBY = 13
    BIN1 = 15
    BIN2 = 16
    PWMB = 18
    allPins = [AIN1, AIN2, PWMA, STBY, BIN1, BIN2, PWMB]
    mPins = [AIN1, AIN2, BIN1, BIN2];
    
    # Declare the GPIO settings
    GPIO.setmode(GPIO.BOARD)

    # Set up GPIO Pins
    setUpPins(allPins)
    
    # Drive motors cw
    driveMultMotors(mPins, 'cw')
    
    # Set motor speed
    setMotorSpeed(allPins)
    
    # Disable standby
    disableStandby(STBY)
    
    # Wait 5 seconds 
    wait(5)
    
    # Reset pins
    reset(allPins)
    
    
    
if __name == "__main__":
    main()

