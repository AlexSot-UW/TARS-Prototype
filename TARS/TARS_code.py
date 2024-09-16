from gpiozero import AngularServo
from time import sleep


servoR = AngularServo(23, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
servoL = AngularServo(25, min_pulse_width = 0.0006, max_pulse_width = 0.0023)
finalAngle = 90
    
torsoIsFront = True
isStanding = True
    
def leftArmMove(val):
    servoL.angle = val
    
def rightArmMove(val):
    servoR.angle = -val
    
def armMove(val):
    servoL.angle = val
    servoR.angle = -val
    
def torsoMove(val):
    servoL.angle = -val
    servoR.angle = val
    
#Moves robot forward
def forward():
    global torsoIsFront
    
    #If torso section of robot is in the front, move the arms forward, otherwise move the torso forward
    if torsoIsFront:
        armMove(finalAngle)
        torsoIsFront = False
    else:
        torsoMove(finalAngle)
        torsoIsFront = True

def stand():
    global torsoIsFront
    global isStanding
    
    if torsoIsFront:
        armMove(0)
    else:
        torsoMove(0)

#Method under construction, do not use:
def turnLeft():
    if isStanding:
        rightArmMove(finalAngle)
        sleep(0.5)

#Method under construction, do not use:
def turnRight():
    print("I cannot do that.")
    
#Method under construction, do not use:
def backward():
    if torsoIsFront:
        print("Can't")
        
stand()
sleep(5)

