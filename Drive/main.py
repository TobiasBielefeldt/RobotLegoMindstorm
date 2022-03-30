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
LmaxSpeed = 60
RmaxSpeed = LmaxSpeed + 3

Lmotor = Motor(Port.A)
Rmotor = Motor(Port.C)

gyroSensor = GyroSensor(Port.S2)
RcolorSensor = ColorSensor(Port.S4)
LcolorSensor = ColorSensor(Port.S1)

isCorrectingLeft = False
isCorrectingRight = False

grace = 2

def intersection():
    return RcolorSensor.color() == Color.BLACK and LcolorSensor.color() == Color.BLACK

def default():
    return RcolorSensor.color() == Color.WHITE and LcolorSensor.color() == Color.WHITE

def slantLeft():
    return RcolorSensor.color() == Color.BLACK and LcolorSensor.color() == Color.WHITE

def slantRight():
    return RcolorSensor.color() == Color.WHITE and LcolorSensor.color() == Color.BLACK

def deliver():
    while not intersection():
        if slantLeft():
            Rmotor.dc(RmaxSpeed-15)
            Lmotor.dc(LmaxSpeed)
        elif slantRight():
            Rmotor.dc(RmaxSpeed)
            Lmotor.dc(LmaxSpeed-15)
        else:
            Rmotor.dc(RmaxSpeed+3)
            Lmotor.dc(LmaxSpeed)
    Rmotor.dc(0)
    Lmotor.dc(0)
    backward()

def backward():
    wait(250)
    for i in range(2):
        while not intersection():
            if slantLeft():
                Rmotor.dc(-RmaxSpeed/2+15)
                Lmotor.dc(-LmaxSpeed/2)
            elif slantRight():
                Rmotor.dc(-RmaxSpeed/2)
                Lmotor.dc(-LmaxSpeed/2+15)
            else:
                Rmotor.dc(-RmaxSpeed)
                Lmotor.dc(-LmaxSpeed)

        while intersection():
            Rmotor.dc(-RmaxSpeed)
            Lmotor.dc(-LmaxSpeed)
        Rmotor.dc(0)
        Lmotor.dc(0)

    wait(250)
    forward()

def turnLeft():
    while gyroSensor.angle() > -90:
        Rmotor.dc(20)
        Lmotor.dc(-15)
    Rmotor.dc(0)
    Lmotor.dc(0)
    gyroSensor.reset_angle(0)

def turnRight():  
    while gyroSensor.angle() < 90:
        Rmotor.dc(-15)
        Lmotor.dc(20)
    Rmotor.dc(0)
    Lmotor.dc(0)
    gyroSensor.reset_angle(0)

def forwardX(count):
    for i in range(count):
        forward()

def simpleForward():
    while not intersection():
        Rmotor.dc(RmaxSpeed)
        Lmotor.dc(LmaxSpeed)
    while intersection():       
        Rmotor.dc(RmaxSpeed)
        Lmotor.dc(LmaxSpeed)
    Rmotor.dc(0)
    Lmotor.dc(0)

def forward():
    while not intersection():
        if slantLeft():
            Rmotor.dc(RmaxSpeed-15)
            Lmotor.dc(LmaxSpeed)
        elif slantRight():
            Rmotor.dc(RmaxSpeed)
            Lmotor.dc(LmaxSpeed-15)
        else:
            Rmotor.dc(RmaxSpeed+3)
            Lmotor.dc(LmaxSpeed)

    while intersection():
        Rmotor.dc(RmaxSpeed)
        Lmotor.dc(LmaxSpeed)

    Rmotor.dc(0)
    Lmotor.dc(0)
    
    

ev3.speaker.beep(frequency=400, duration=200)
#wait(7000)
gyroSensor.reset_angle(0)

while True:
    print(str(gyroSensor.angle()))

