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
maxSpeed = 60
turnSpeed = 30

Lmotor = Motor(Port.A,Direction.COUNTERCLOCKWISE)
Rmotor = Motor(Port.C,Direction.COUNTERCLOCKWISE)

gyroSensor = GyroSensor(Port.S3)
RcolorSensor = ColorSensor(Port.S1)
LcolorSensor = ColorSensor(Port.S4)

isArmUp = True
isCorrectingLeft = False
isCorrectingRight = False

grace = 2

def intersection():
    return RcolorSensor.color() == Color.BLACK and LcolorSensor.color() == Color.BLACK

def default():
    return RcolorSensor.color() == Color.WHITE and LcolorSensor.color() == Color.WHITE

def slantLeft():
    global isCorrectingLeft
    if (gyroSensor.angle() > grace):
        isCorrectingLeft = True
        return True
    elif (isCorrectingLeft and gyroSensor.angle() > 0):
        return True
    else:
        isCorrectingLeft = False
        return False

def slantRight():
    global isCorrectingRight
    if (gyroSensor.angle() < -grace):
        isCorrectingRight = True
        return True
    elif (isCorrectingRight and gyroSensor.angle() < 0):
        return True
    else:
        isCorrectingRight = False
        return False

def slantLeft():
    return gyroSensor.angle() < -grace

def slantRight():
    return gyroSensor.angle() > grace

def backward():
    for i in range(2):
        while not intersection():
            if slantRight():
                Rmotor.dc(-maxSpeed*0.7)
                Lmotor.dc(-maxSpeed)
            elif slantLeft():
                Rmotor.dc(-maxSpeed)
                Lmotor.dc(-maxSpeed*0.7)
            else:
                Rmotor.dc(-maxSpeed)
                Lmotor.dc(-maxSpeed)

        while intersection():
            Rmotor.dc(-maxSpeed)
            Lmotor.dc(-maxSpeed)

        Rmotor.dc(0)
        Lmotor.dc(0)

def turnLeft():
    while gyroSensor.angle() > -90:
        Rmotor.dc(50)
        Lmotor.dc(8)
    Rmotor.dc(0)
    Lmotor.dc(0)
    gyroSensor.reset_angle(0)

def turnRight():  
    while gyroSensor.angle() < 45:
        Rmotor.dc(-5)
        Lmotor.dc(50)
    while gyroSensor.angle() < 90:
        Rmotor.dc(5)
        Lmotor.dc(50)
    Rmotor.dc(0)
    Lmotor.dc(0)
    gyroSensor.reset_angle(0)

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

def simpleForward():
    while not intersection():
        Rmotor.dc(maxSpeed)
        Lmotor.dc(maxSpeed)
    while intersection():
        
        Rmotor.dc(maxSpeed)
        Lmotor.dc(maxSpeed)
    Rmotor.dc(0)
    Lmotor.dc(0)

def forward():
    while not intersection():
        if slantLeft():
            Rmotor.dc(maxSpeed-15)
            Lmotor.dc(maxSpeed)
        elif slantRight():
            Rmotor.dc(maxSpeed)
            Lmotor.dc(maxSpeed-15)
        else:
            Rmotor.dc(maxSpeed)
            Lmotor.dc(maxSpeed)

    while intersection():
        Rmotor.dc(maxSpeed)
        Lmotor.dc(maxSpeed)

    Rmotor.dc(0)
    Lmotor.dc(0)
    
    

ev3.speaker.beep(frequency=400, duration=200)
wait(7000)
gyroSensor.reset_angle(0)
forward()
forward()
forward()
turnRight()    
