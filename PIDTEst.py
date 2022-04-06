from time import time
currentValue = 0

startTime = time()
errorPrev = 0
errorSum = 0

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


for i in range(50):
    u = PID(100,0.5,0.5,0.5,currentValue)
    currentValue = currentValue + u
    print(u)
