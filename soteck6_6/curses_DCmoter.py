import RPi.GPIO as GPIO
import time
import curses

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwmoutput = GPIO.PWM(18, 50)
pwmoutput.start(0)
#GPIO.

def main(stdscr):
    
    fanduty =0
    pow_ind = ''
    stdscr.addstr(0, 0, '[a]:speed up [z]:speed down [q]:quit')
    stdscr.addstr(1, 0, 'POW:')

    while True :
        c = stdscr.getch()
        if (c == ord('a')) and (fanduty < 100):
            fanduty +=10
            pwmoutput.ChangeDutyCycle(fanduty)
            pow_ind += ' '
            stdscr.addstr(1,4,pow_ind,curses.A_REVERSE)

        elif (c == ord('z')) and (fanduty < 100):
            fanduty -=10
            pwmoutput.ChangeDutyCycle(fanduty)
            pow_ind = pow_ind[0:len(pow_ind)-1]
            stdscr.addstr(1,4,pow_ind,curses.A_REVERSE)
            stdscr.clrtoeol()

        elif c == ord('q'):
            break;

if __name__ == '__main__':
    curses.wrapper(main)
    pwmoutput.stop()
