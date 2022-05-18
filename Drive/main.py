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

errorSum = 0

turnSpeed = 50

forwardSpeed = 70

#Define motors
Lmotor = Motor(Port.C)
Rmotor = Motor(Port.A)

#Define sensors
gyroSensor = GyroSensor(Port.S1)
backLightSensor = ColorSensor(Port.S2)
frontLightSensor = ColorSensor(Port.S3)


colourList = [Color.WHITE,Color.WHITE,Color.WHITE]
count = 0


def isBlack():
    global colourList
    for x in colourList:
        if(x != Color.BLACK):
            return False
    return True

def intersection():
    global colourList
    global count
    colourList[count] = backLightSensor.color()
    print(colourList)
    count += 1
    if (count == len(colourList)):
        count = 0
    return isBlack()

def turnLeft():
    gyroSensor.reset_angle(0)
    while gyroSensor.angle() > -76:
        Rmotor.dc(turnSpeed)
        Lmotor.dc(-turnSpeed)
    Rmotor.dc(0)
    Lmotor.dc(0)
    resetPID()
    
def deliver():
    forward()
    Rmotor.dc(forwardSpeed)
    Lmotor.dc(forwardSpeed)
    wait(180)
    Rmotor.dc(0)
    Lmotor.dc(0)
    wait(10)
    Rmotor.dc(-forwardSpeed)
    Lmotor.dc(-forwardSpeed)
    wait(180)    
    Rmotor.dc(0)
    Lmotor.dc(0)

def turnRight():  
    gyroSensor.reset_angle(0)
    while gyroSensor.angle() < 76:
        Rmotor.dc(-turnSpeed)
        Lmotor.dc(turnSpeed)
    Rmotor.dc(0)
    Lmotor.dc(0) 
    resetPID()   
    

def resetPID():
    global errorSum
    global startTime
    errorSum = 0
    startTime = time()

def forward():
    k = 1
    K_P = 0.42
    K_I = 0.002
    while not intersection():
        u = PINoD(goal,K_P,K_I,frontLightSensor.reflection())
        Rmotor.dc(forwardSpeed+k*u)
        Lmotor.dc(forwardSpeed-k*u)

    while intersection():
        u = PINoD(goal,K_P,K_I,frontLightSensor.reflection())
        Rmotor.dc(forwardSpeed+k*u)
        Lmotor.dc(forwardSpeed-k*u)

    Rmotor.dc(0)
    Lmotor.dc(0)

def Turn180():
    gyroSensor.reset_angle(0)
    while gyroSensor.angle() < 167:
        Rmotor.dc(-turnSpeed)
        Lmotor.dc(turnSpeed)
    Rmotor.dc(0)
    Lmotor.dc(0) 
    resetPID()  

#We were told to ignore D in PID
def PINoD(goal,K_P,K_I,inputValue):
    global startTime
    global errorSum
    u = 0 
    
    stopTime = time()
    deltaTime = stopTime - startTime
    
    error = goal - inputValue

    #Estimator for integral
    errorSum = errorSum + error * deltaTime
    u += K_I * errorSum
        
    #Proporitnal
    u += K_P * error
    
    #Update for next iteration
    startTime = time()
    
    return u


ev3.speaker.beep(frequency=400, duration=200)
wait(1000)
#Black has a reflection of about 3 while white is about 50 so the goal is in between
startTime = time()
goal = 21
gyroSensor.reset_angle(0)





# Generated Code starts here. Please don't remove or modify any code at this point.
def runSolution():
	turnLeft()
	forward()
	forward()
	forward()
	forward()
	turnRight()
	deliver()
	Turn180()
	forward()
	forward()
	turnRight()
	forward()
	forward()
	turnRight()
	forward()
	turnRight()
	forward()
	forward()
	forward()
	forward()
	deliver()
	turnRight()
	forward()
	turnLeft()
	forward()
	turnLeft()
	forward()
	deliver()
	turnRight()
	forward()
	turnLeft()
	forward()
	forward()
	turnLeft()
	forward()
	forward()
	turnLeft()
	forward()
	turnLeft()
	forward()
	deliver()
	Turn180()
	forward()
	turnLeft()
	forward()
	forward()
	turnRight()
	forward()
	forward()
	turnRight()
	forward()
	turnLeft()
	deliver()
	turnRight()
	forward()
	forward()
	turnLeft()
	forward()
	forward()
	turnLeft()
	forward()
	deliver()
	turnLeft()
	deliver()
	Turn180()
	forward()
	turnRight()
	forward()
	forward()
	turnRight()
	forward()
	forward()
	turnRight()
	forward()
	deliver()
	turnRight()
	forward()
	turnLeft()
	forward()
	turnLeft()
	forward()
	forward()
	deliver()
	turnRight()
	forward()
	turnLeft()
	forward()
	turnLeft()
	forward()
	deliver()
	turnRight()
	forward()
	turnLeft()
	forward()
	forward()
	turnLeft()
	forward()
	forward()
	turnLeft()
	forward()
	turnLeft()
	deliver()
	turnLeft()
	forward()
	turnRight()
	forward()
	turnRight()
	deliver()
	Turn180()
	forward()
	turnRight()
	forward()
	forward()
	turnRight()
	forward()
	turnRight()
	deliver()
	turnRight()
	forward()
	turnLeft()
	forward()
	forward()
	turnLeft()
	forward()
	forward()
	forward()
	turnRight()
	forward()
	forward()
	forward()
	forward()
	turnLeft()
	forward()
	turnRight()
	forward()
	forward()
	turnRight()
	forward()
	turnRight()
	forward()
	forward()
	forward()
	forward()
	deliver()
	turnRight()
	forward()
	turnLeft()
	forward()
	turnLeft()
	forward()
	deliver()
	Turn180()
	forward()
	turnRight()
	forward()
	forward()
	forward()
	forward()
	forward()
	turnRight()
	forward()
	forward()
	forward()
	turnRight()
	forward()
	turnRight()
	forward()
	deliver()
	turnRight()
	forward()
	turnLeft()
	forward()
	turnLeft()
	forward()
	forward()
	forward()
	deliver()
	turnRight()
	forward()
	turnLeft()
	forward()
	turnLeft()
	deliver()

runSolution()
# Generated Code ended. You may edit again.