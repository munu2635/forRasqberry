import RPi.GPIO as GPIO
import sensor
import testNoPin # node 

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#mainInstance = sensor.Sensor(GPIO)
mainInstance = testNoPin.Sensor(GPIO)

def startToSensing():
		mainInstance.sensing()

try:
	while True:
		startToSensing()

except KeyboardInterrupt:
	GPIO.cleanup()