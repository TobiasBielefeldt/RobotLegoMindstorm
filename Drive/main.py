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
armMotor = Motor(Port.B)

gyroSensor = GyroSensor(Port.S3)
RcolorSensor = ColorSensor(Port.S1)
LcolorSensor = ColorSensor(Port.S4)

isArmUp = True

grace = 7

gyroSensor.reset_angle(0)

def intersection():
    return RcolorSensor.color() == Color.BLACK and LcolorSensor.color() == Color.BLACK

def default():
    return RcolorSensor.color() == Color.WHITE and LcolorSensor.color() == Color.WHITE

def slantLeft():
    return gyroSensor.angle() > grace

def slantRight():
    return gyroSensor.angle() < -grace

def turnLeft():
    state = 0
    while True:
        if LcolorSensor.color() == Color.BLACK and state == 0:
            state = 1
        elif LcolorSensor.color() == Color.WHITE and state == 1:
            return
        Rmotor.dc(30)
        Lmotor.dc(-30)

    Rmotor.dc(0)
    Lmotor.dc(0)      

        
def turnRight():
    state = 0
    while True:
        if RcolorSensor.color() == Color.BLACK and state == 0:
            state = 1
        elif RcolorSensor.color() == Color.WHITE and state == 1:
            return

        Rmotor.dc(-30)
        Lmotor.dc(30)

def backward():
    for i in range(2):
        while not intersection():
            if slantRight():
                Rmotor.dc(-60)
                Lmotor.dc(-80)
            elif slantLeft():
                Rmotor.dc(-80)
                Lmotor.dc(-60)
            else:
                Rmotor.dc(-80)
                Lmotor.dc(-80)

        while intersection():
            Rmotor.dc(-80)
            Lmotor.dc(-80)

        Rmotor.dc(0)
        Lmotor.dc(0)

def turnRight():
    gyroSensor.reset_angle(0)
    while gyroSensor.angle() < 90:
        Rmotor.dc(80)
        Lmotor.dc(17)
    Rmotor.dc(0)
    Lmotor.dc(0)

def turnLeft():
    gyroSensor.reset_angle(0)
    while gyroSensor.angle() > -90:
        Rmotor.dc(17)
        Lmotor.dc(80)
    Rmotor.dc(0)
    Lmotor.dc(0)

def forwardX(count):
    for i in range(count):
        forward()

def toggleArm():
    global isArmUp
    if isArmUp:
        armMotor.run_angle(150, -200)
    else:
        armMotor.run_angle(150, 200)
    isArmUp = not isArmUp
    armMotor.stop()

def forward():
    gyroSensor.reset_angle(0)
    while not intersection():
        if slantLeft():
            Rmotor.dc(10)
            Lmotor.dc(30)
        elif slantRight():
            Rmotor.dc(30)
            Lmotor.dc(10)
        else:
            Rmotor.dc(80)
            Lmotor.dc(80)

    while intersection():
        Rmotor.dc(80)
        Lmotor.dc(80)

    Rmotor.dc(0)
    Lmotor.dc(0)
    
    

ev3.speaker.beep(frequency=400, duration=200)
wait(1000)

#forwardX(2)
#backward()

toggleArm()
toggleArm()

#forward()
#turnRight()

