from acm1602 import acm1602
import time

lcd = acm1602(1, 0x50, 4)
lcd.move_home()
lcd.set_cursol(0)
lcd.set_blink(0)

lcd.backlight(1)

lcd.move(0x00, 0x00)
lcd.write('アイウエオカキクケコサシスセソ')
lcd.move(0x00, 0x01)
lcd.write('タチツテトナニヌネノハヒフヘホ')
time.sleep(5)

lcd.move(0x00, 0x00)
lcd.write('マミムメモヤユヨラリルレロワヲン')
lcd.move(0x00, 0x01)
lcd.write("゛゜千万円÷          ")
time.sleep(5)

lcd.move(0x00, 0x00)
lcd.write('アイウエオカキクケコサシスセソ')
lcd.write("。「」、・                     ")
lcd.move(0x00, 0x01)
lcd.write("ヲァィゥェォャュョッー         ")
