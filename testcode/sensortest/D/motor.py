import RPi.GPIO as GPIO
import time

motor1_pin = 17
motor2_pin = 27


GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin, GPIO.OUT)
GPIO.setup(motor2_pin, GPIO.OUT)

p1 = GPIO.PWM(motor1_pin, 50)
p2 = GPIO.PWM(motor2_pin, 50)

p1.start(0)
p2.start(0)

cnt = 0

try:

    while True:

	p1.ChangeDutyCycle(10.0)
	time.sleep(1)
	p1.ChangeDutyCycle(7.5)
	time.sleep(1)
	p2.ChangeDutyCycle(5.0)
	time.sleep(1)
#	p2.ChangeDutyCycle(6.0)
	time.sleep(1)

        p1.ChangeDutyCycle(5.0)
        time.sleep(3)


except KeyboardInterrupt:
    print("end")
    GPIO.cleanup()
    p1.stop()
    p2.stop()
