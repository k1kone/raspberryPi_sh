import RPi.GPIO as GPIO
import dht11
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=17)

while True:
    result = instance.read()
    if result.is_valid():
        print('Last valid input:' + str(datetime.datetime.now()))
        print('Temperature:{}C'.format(result.temperature))
        print('Humidity:{}%'.format(result.humidity))

    time.sleep(3)
