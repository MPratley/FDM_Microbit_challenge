from microbit import *
import radio

leftWheelPWM = pin0
rightWheelPWM = pin1

leftWheelDirection = pin8
rightWheelDirection = pin12

def forwards():
    rightWheelDirection.write_digital(0)
    leftWheelDirection.write_digital(0)
    
def backwards():
    rightWheelDirection.write_digital(1)
    leftWheelDirection.write_digital(1)
    
def turn_left():
    leftWheelPWM.write_analog(255)
    rightWheelPWM.write_analog(120)
    
def turn_right():
    leftWheelPWM.write_analog(120)
    rightWheelPWM.write_analog(255)

def 

radio.on()
radio.config(group=45)

while True:
    incoming_msg = radio.receive()
    if incoming_msg:
        leftWheelPWM.write_analog(incoming_msg[0])
        rightWheelPWM.write_analog(incoming_msg[1])
    