import RPi.GPIO as GPIO          
from time import sleep
from getch import getch


## in1 in2 left side
## in3 in4 right side

in1 = 27 #yellow
in2 = 22 #green
in3 = 16 #brown
in4 = 20 #white
enb = 21 #purple
ena = 17 #green


GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)


GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)


p1 = GPIO.PWM(ena,200)
p2 = GPIO.PWM(enb,200)

p1.start(50)
p2.start(50)
print("\n")
print("f-forward s-stop l-leftTurn r-rightTurn")
print("\n")    

sleepingTime = 0.5

def stop():
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

def forward():
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        sleep(sleepingTime)
        stop()

def left():
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        sleep(sleepingTime)
        stop()


def right():
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)  
        sleep(sleepingTime)
        stop()


def backward():
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        sleep(sleepingTime)
        stop()



# while(1):
#     x = getch()
#     if x=='w':
#         forward()
#         stop()
#         x='z'


#     elif x==' ':
#         stop()
        
#         x='z'

#     elif x=='a':
#         left()
#         stop()
#         x = "z"
        

#     elif x=='s':
#         backward()
#         stop()
#         x='z'

#     elif x=='d':
#         right()
#         stop()
#         x = "z"

#     elif x=='e':
#         GPIO.cleanup()
#         break
    
#     else:
#         print("<<<  wrong data  >>>")
#         print("please enter the defined data to continue.....")
