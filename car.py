from microbit import *
import radio
import neopixel

leftWheelPWM = pin0
rightWheelPWM = pin1

leftWheelDirection = pin8
rightWheelDirection = pin12

radio.on()
radio.config(group=46)

def beep():
    pin14.write_analog(120)
    sleep(200)
    pin14.write_analog(0)
    sleep(200)
    pin14.write_analog(120)
    sleep(200)
    pin14.write_analog(0)
    sleep(200)
    pin14.write_analog(200)
    sleep(400)
    pin14.write_analog(0)
    
beep()

while True:
    incoming_msg = radio.receive()
    if incoming_msg:
        incoming_msg = str(incoming_msg)
        print(incoming_msg)
        print(incoming_msg.split(","))
        speedArray = list(map(int, incoming_msg.split(",")))
        leftWheelPWM.write_analog(speedArray[0])
        rightWheelPWM.write_analog(speedArray[1])
    