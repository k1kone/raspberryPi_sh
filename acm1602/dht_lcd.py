import RPi.GPIO as GPIO
import dht11
import time
import datetime
from acm1602 import acm1602


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

lcd = acm1602( 1, 0x50, 4 )
lcd.move_home()
lcd.set_cursol( 0 )
lcd.set_blink( 0 )
lcd.backlight(1)
ins = dht11.DHT11(pin=17)
txt =''
i=0

result = ins.read()
if result.is_valid():
    txt = 'Temp:' + str(result.temperature) + chr(0xdf)+'C '+'RM:'+ str(result.humidity) + '%' 
    print(time.strftime('%p %I:%M:%S %a') + ' [' + txt + ' ]')
else:
    print('***can\'t get date.***')




while True:
    if i>=3:
        result = ins.read()
        if result.is_valid():
            txt = 'Temp:' + str(result.temperature) + chr(0xdf)+'C '+'RM:'+ str(result.humidity) + '%' 
            print(time.strftime('%p %I:%M:%S %a') + ' [' + txt + ' ]')
        else:
            print('***can\'t get date.***')
        i=0
    lcd.move( 0x00, 0x00 )
    lcd.write(time.strftime('%p %I:%M:%S %a'))
    lcd.move( 0x00, 0x01 )
    lcd.write(txt)
    i+=1
    time.sleep(1)

