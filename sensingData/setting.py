
raspid = "test1"

brokerIpPort = ["124.139.136.86", "1883"]

cameraGlobalport = "8891"
cameraLocalport = "8891"

useSensor = [True, True, True, True, False, False, True, True, True ]
 # dht11 / fire / shock / ir / gas / cds / button / led / motor

all_pin = [22, 25, 24, 23, 27, 16, 26, 6, 5, 20, 21]
	# dht11_pin = 22 / fire_pin = 25 / led_red_pin = 24 / led_green_pin = 23
	# shock_pin = 27 / ir_sensor_pin = 16 / button_pin = 26 / gas_pin = 6
	# cds_pin = 5 / motor_pin_1 = 20 / motor_pin_2 = 21

sensordata = [all_pin, useSensor]

# dev server IP
# brokerIpPort = ["124.139.136.86", "1883"]

# test server IP
#brokerIpPort = ["115.20.144.97", "11183"]ttt

