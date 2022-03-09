#!/usr/bin/env pybricks-micropython
#from locale import LC_ALL
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

Rmotor = Motor(Port.A,Direction.COUNTERCLOCKWISE)
Lmotor = Motor(Port.D,Direction.COUNTERCLOCKWISE)

#gyroSensor = GyroSensor(Port.S1)
RcolorSensor = ColorSensor(Port.S1)
LcolorSensor = ColorSensor(Port.S4)
    
#gyroSensor.reset_angle(0)

def intersection():
    return RcolorSensor.color() == Color.BLACK and LcolorSensor.color() == Color.BLACK

def slantRight():
    return LcolorSensor.color() == Color.BLACK and RcolorSensor.color() == Color.WHITE

def slantLeft():
    return LcolorSensor.color() == Color.WHITE and RcolorSensor.color() == Color.BLACK

def turnLeft():
    state = 0
    while True:
        if LcolorSensor.color() == Color.BLACK and state == 0:
            state = 1
        elif LcolorSensor.color() == Color.WHITE and state == 1:
            return

        Rmotor.dc(30)
        Lmotor.dc(-30)

        
def turnRight():
    state = 0
    while True:
        if RcolorSensor.color() == Color.BLACK and state == 0:
            state = 1
        elif RcolorSensor.color() == Color.WHITE and state == 1:
            return

        Rmotor.dc(-30)
        Lmotor.dc(30)
        

def forward(steps):
    for i in range(steps):
        while not intersection():
            if slantLeft():
                Rmotor.dc(10)
                Lmotor.dc(30)
            elif slantRight():
                Rmotor.dc(30)
                Lmotor.dc(10)
            else:
                Rmotor.dc(20)
                Lmotor.dc(  20)
        wait(400)
        
    

ev3.speaker.beep(frequency=1000, duration=500)

forward(2)
turnLeft()
forward(1)
