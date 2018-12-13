import smbus, time
from acm1602 import acm1602

lcd = acm1602(1, 0x50, 4)

lcd.move_home()
lcd.set_cursol(0)
lcd.set_blink(0)
lcd.backlight(1)
lcd.write('Ras PI')
lcd.move(0x00, 0x01)
while True:
    lcd.move(0x00, 0x01)
    lcd.write(time.strftime('%H:%M:%S'))
    time.sleep(1)
