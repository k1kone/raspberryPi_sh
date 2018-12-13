import RPi.GPIO as GPIO
import time
import curses


GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwmoutput = GPIO.PWM(18, 50)

pwmoutput.start(0)

stdscr = curses.initscr()

curses.noecho()

fanduty = 0

while True :
    c = stdscr.getch()
    if (c == ord('a')) and (fanduty < 100):
        fanduty += 10
        pwmoutput.ChangeDutyCycle(fanduty)
        
    elif (c == ord('z')) and (fanduty > 0):
        fanduty -= 10
        pwmoutput.ChangeDutyCycle(fanduty)

    elif c == ord('q'):
        break;

pwmoutput.stop()

curses.echo()

curses.endwin()
