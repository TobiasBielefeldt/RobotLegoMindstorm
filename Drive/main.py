#!/usr/bin/env pybricks-micropython
#from locale import LC_ALL
from time import time
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
startTime = time()
errorPrev = 0
errorSum = 0

Lmotor = Motor(Port.C)
Rmotor = Motor(Port.A)

gyroSensor = GyroSensor(Port.S1)
backLightSensor = ColorSensor(Port.S2)
frontLightSensor = ColorSensor(Port.S3)

isCorrectingLeft = False
isCorrectingRight = False

grace = 2

def intersection():
    return backLightSensor.color() == Color.BLACK

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
    while gyroSensor.angle() > -85:
        Rmotor.dc(35)
        Lmotor.dc(-35)
    Rmotor.dc(0)
    Lmotor.dc(0)
    gyroSensor.reset_angle(0)

def turnRight():  
    while gyroSensor.angle() < 85:
        Rmotor.dc(-35)
        Lmotor.dc(35)
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

def resetPID():
    errorPrev = 0
    errorSum = 0
    startTime = time()

def forward():
    resetPID()
    k = 1
    K_P = 0.4
    K_I = 0.1
    K_D = 0
    speed = 50
    while not intersection():
        u = PID(goal,K_P,K_I,K_D,frontLightSensor.reflection())
        Rmotor.dc(speed+k*u)
        Lmotor.dc(speed-k*u)

    while intersection():
        u = PID(goal,K_P,K_I,K_D,frontLightSensor.reflection())
        Rmotor.dc(speed+k*u)
        Lmotor.dc(speed-k*u)

    
    Rmotor.dc(speed+k*u)
    Lmotor.dc(speed-k*u)

def PID(goal,K_P,K_I,K_D,inputValue):
    global startTime
    global errorPrev
    global errorSum
    u = 0
    
    stopTime = time()
    deltaTime = stopTime - startTime
    
    error = goal - inputValue
    #Estimator for integral
    errorSum = errorSum + error * deltaTime
    u += K_I * errorSum
    
    #Estimator for  derivative
    if(deltaTime < 0.0 or deltaTime > 0.0):
        dedt = ( error - errorPrev ) / deltaTime
        u += K_D * dedt
        
    #Proporitnal
    u += K_P * error
    
    #Update for next iteration
    errorPrev = error
    startTime = time()
    
    
    return u


ev3.speaker.beep(frequency=400, duration=200)
wait(7000)
ev3.speaker.beep(frequency=400, duration=200)
goal = frontLightSensor.reflection()

forward()
forward()
forward()
forward()
turnRight()
forward()
turnLeft()
forward()
turnLeft()
forward()
forward()
turnLeft()
forward()
turnRight()
forward()
forward()
forward()
forward()
