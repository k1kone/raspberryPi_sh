from bottle import route, run
import RPi.GPIO as GPIO

host = 'localhost'
p = 8080

GPIO.setmode(GPIO.BCM)
led_pin = [18, 23, 24]
led_states = [0, 0, 0]
switch_pin = 25

for i in led_pin:
    GPIO.setup(i, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def switch_status():
    state = GPIO.input(switch_pin)
    print('switch_status = {}'.format(state))
    if state:
        return 'UP'
    else:
        return 'DOWN'

def html_for_led(led):
    l = str(led)
    result = '<input type="button" onClick="changed(' + l + ')" value="LED' + l + '"/>'
    return result


def update_leds():
    for i, value in enumerate(led_states):
        GPIO.output(led_pin[i], value)

@route('/')
@route('/<led>')
def index(led='n'):
    print(led)
    if led !='n':
        try:
            led_num = int(led)
            led_states[led_num] = not led_states[led_num]
            update_leds()
        except ValueError:
            print('Faliure w/led = ' + led)
    respons = '''
                <script>
                    function changed(led){
                        window.location.href = '/' + led;
                        }
                </script>
                <h1>GPIO Control</h1>'''
    respons += '<h2>Button = ' + switch_status() + '</h2>' 
    respons += '<h2>LEDs</h2>' 
    for i in range(len(led_pin)):
        respons += html_for_led(i)
    return respons

run(host=host, port=p)

