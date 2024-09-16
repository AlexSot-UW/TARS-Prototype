#Name: TARS_Graphics.py
#Creator: Alexander Sotnikov
#Date: January 6, 2024
#Description: Basic code which creates a simple gui interface, that allows the user to control the robot (similar to a remote control)

import PySimpleGUI as sg
from TARS_code import forward,backward,left,right,stand

buttonSizeX = 7
buttonSizeY = 3

#Creates the three columns that make up the graphical user interface
controlsLeft = [[sg.Button("Turn Left", size=(buttonSizeX,buttonSizeY), key="L")]]

controlsForwardBackward = [[sg.Button("Forward", size=(buttonSizeX,buttonSizeY), key="F")], [sg.Button("Backward", size=(buttonSizeX,buttonSizeY), key="B")]]

controlsRight = [[sg.Button("Turn Right", size=(buttonSizeX,buttonSizeY), key="R")]]

# Create the windo wlayout
layout = [[sg.Column(controlsLeft),sg.VSeperator(),sg.Column(controlsForwardBackward),sg.VSeperator(),sg.Column(controlsRight)]]

# Create the window
window = sg.Window("TARS Controller", layout)

#

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window
    # If statement controls the movement of the TARS arms and torso using the methods from the TARS_code class
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "F":
        print("Forward")
        forward()
    elif event == "B":
        print("Backward")
        backward()
    elif event == "L":
        print("Left")
        turnLeft()
    elif event == "R":
        print("Right")
        turnRight()
        
window.close()