from microbit import *
import radio

# Turns on radio
radio.on()
radio.config(group=46)

#initialise variable
toSend = ""
last = ""

speed = 0
direction = "straight"

while True:
    direction = "straight"
    speed = 0
    
    if accelerometer.get_x() < -400:
        direction = "left"
        
        
    if accelerometer.get_x() > 400:
        direction = "right"
     
    if button_a.is_pressed():      
        speed = 600
    

       
    
    if direction == "left":
        toSend = str(int(speed / 5)) + ',' + str(speed)
    elif direction == "right":
        toSend = str(speed) + ',' + str(int(speed / 5))
    else: 
        toSend = str(speed) + ',' + str(speed)
        
    if toSend != last:    
        radio.send(toSend)
        last = toSend
        sleep(50)
    

