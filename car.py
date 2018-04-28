from microbit import *
import radio

def forwards():
    pin12.write_digital(0)
    pin8.write_digital(0)
    
def backwards():
    pin12.write_digital(1)
    pin8.write_digital(1)
    
def left():
    pin0.write_analog(255)
    pin1.write_analog(120)
    
    
def right():
    pin0.write_analog(120)
    pin1.write_analog(255)

radio.on()
radio.config(group=45)

#radio.receive
pin0.write_analog(255)
pin1.write_analog(255)

while True:
    print("hello")
    forwards()
    right()
    

# Write your code here :-)