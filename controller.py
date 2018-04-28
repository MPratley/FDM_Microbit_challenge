from microbit import *

radio.on()
radio.config(group=45)

toSend = [0, 0]
speed = 0

while True:
    if button_a.was_pressed():
        speed = 255
        toSend = [speed,speed]
        radio.send(toSend)