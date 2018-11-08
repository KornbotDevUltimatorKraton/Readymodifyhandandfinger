# Author: Mr. Chanapai Chuadchum 
# Project name: Robotic hand control function 
# Latest update:  time 11:44/date 6/11/2018   
import math  # Math function for the kinematic calculation
import scipy # function for the mat calculation using  
from nanpy import (ArduinoApi,SerialManager) 
import serial #for the sensor input function for the snsory control
from nanpy import Servo # imort servo function 
import time 
import pyttsx # For the speech synthesys function speaking function enable 
import sklearn 
import csv # csv data communication 
import progressbar # Progress bar 
import speech_recognition as sr 
engine = pyttsx.init()
#voices = engine.getProperty('voices')
#for voice in voices:
 #    engine.setProperty('voice',voice.id)
  #   print voice.id
# Servo input function 
servo =  Servo(2)  # Finger 1
servo2 = Servo(3) # Finger 2 
servo3 = Servo(4) # Finger 3 
servo4 = Servo(5) # Finger 4 
servo5 = Servo(6) # Finger 5 
servo6 = Servo(9) # Finger 6
  
try:
   Handfinger = SerialManager('/dev/ttyACM0',115200)  # Hand serial checker and hand shake connection 
   Handcontrol = ArduinoApi(connection=Handfinger)
   engine.say("Hardware serial connected 100 percent")
   engine.runAndWait()
   for i in progressbar.progressbar(range(100)):
          time.sleep(0.02)      
except: 
   print("Connection error please check the serial communication")
try:
  Sensorserial = serial.Serial("/dev/ttyUSB0",115200) # Serial communication for the sensors serial 
  engine.say("Sensors serial connected 100 percent")
  engine.runAndWait()
  for i in progressbar.progressbar(range(100)):
               time.sleep(0.02)      
except: 
  print("Sensors serial failure please check the sensors serial port") 
def Finger1_force_sensor(fsr1):   # Force senssor reading from the fsr 1
         ForceFing1 = (fsr1/4095)*100   # Force finger 1 out function for the force sensor 1 
         return ForceFing1    #return finger1 force 
def Finger2_force_sensor(fsr2):   # Force sensor reading from the fsr 2
         ForceFing2 = (fsr2/4095)*100  # Force finger 2 out function for the force sensor 2   
         return ForceFing2    #return  finger2 force 
def Finger3_force_sensor(fsr3):   # Force sensor reading from the fsr 3
         ForceFing3 = (fsr3/4095)*100  # Force finger 3 out function for the force sensor 3
         return ForceFing3           
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
while True: 
     #delimeter split the data from the  serial communication system 
   try:
     Sensory = Sensorserial.readline() 
     Sensory.split(",")  
     Sensorydata = Sensory.split(",")  # Splitting the sensors 
     Sensor1_feild_sense = Sensorydata[0]
     Sensor2_feild_sense = Sensorydata[1] 
     Sensor3_feild_sense = Sensorydata[2]
     Sensor4_feild_sense = Sensorydata[3] 
     Sensor5_feild_sense = Sensorydata[4]
     Sensor6_feild_sense = Sensorydata[5]
     # Raw data from the MCU ESP32 or any type of 32 bit mcu for higher resolution sense
     print('Sensor1:'+Sensor1_feild_sense)
     print('Sensor2:'+Sensor2_feild_sense)
     print('Sensor3:'+Sensor3_feild_sense)
     print('Sensor4:'+Sensor4_feild_sense)
     print('Sensor5:'+Sensor5_feild_sense)
     print('Sensor6:'+Sensor6_feild_sense)
     Mem1 = {","}   # Memory short time change per event control 
     Mem1.add(int(Sensor1_feild_sense))
     Mem1.add(int(Sensor2_feild_sense))
     Mem1.add(int(Sensor3_feild_sense))
     Mem1.add(int(Sensor4_feild_sense))
     Mem1.add(int(Sensor5_feild_sense))
     Mem1.add(int(Sensor6_feild_sense))
     print(Mem1)
     print("Number of sensor"+ str(int(len(Mem1))-1)) # Len will detected and calculate the joint number to running 1 time for the detection 
     #stop_listening = r.listen_in_background(m,callback) 
     # Sensor1 condition working control application  
     if int(Sensor1_feild_sense) >= 600:
        #if 4095 in Mem1 == "True":
          engine.say('I feel touch ')
          engine.runAndWait()
          for move in [45,90]:      
            servo.write(move) 
            servo2.write(move+20)
            servo3.write(move+30)
            servo4.write(90-move)  
            servo5.write(move+10)
            servo6.write(move)
            print("finger1 Angle:"+ str(move)) 
            time.sleep(0.1) 
            
     else: 
         print("Sensor1 feild sense waiting status......."+ "[" +str(Sensor1_feild_sense) + "]") 
         print("Sensor2 feild sense waiting status......."+ "[" +str(Sensor2_feild_sense) + "]")
         print("Sensor3 feild sense waiting status......."+ "[" +str(Sensor3_feild_sense) + "]") 
         print("Sensor4 feild sense waiting status......."+ "[" +str(Sensor4_feild_sense) + "]")
         print("Sensor5 feild sense waiting status......."+ "[" +str(Sensor5_feild_sense) + "]") 
         print("Sensor6 feild sense waiting status......."+ "[" +str(Sensor6_feild_sense) + "]")
   except:
     print("Error sensoryfunction") 
    
          
    
