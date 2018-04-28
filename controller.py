from microbit import *
import radio

radio.on()
radio.config(group=46)

toSend = ""
speed = 0
direction = "straight"

while True:
    if accelerometer.get_x() < -200:
        direction = "left"
        
        
    if accelerometer.get_x() > 200:
        direction = "right"
     
    if button_a.was_pressed():      
        speed = 255
    
    if button_b.was_pressed():
        speed = 0
    
    if direction == "left":
        toSend = str(0) + ',' + str(speed)
    
    if direction == "right":
        toSend = str(speed) + ',' + str(0)
        
    radio.send("100,100")
    
    speed = 0
    direction = "straight"