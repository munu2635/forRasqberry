import RPi.GPIO as GPIO
import sensor
import testNoPin # node
import os

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

localGlobalIp = os.popen('curl ifconfig.me').read()
# localIp = os.popen('hostname -I').read() ## ip

cameraCheck = os.system('sh /home/pi/raspstart/mjpg.sh &')
# mainInstance = sensor.Sensor(GPIO, localGlobalIp)
mainInstance = testNoPin.Sensor(GPIO, localGlobalIp)

def startToSensing():
		mainInstance.sensing()

try:
	print("start")
	while True:
		startToSensing()

except KeyboardInterrupt:
	GPIO.cleanup()
