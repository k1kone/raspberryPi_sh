import serial
import time

def main():
    con = serial.Serial('/dev/ttyACM0',9600)
    time.sleep(1)
    print (con.portstr)
    hello_str = 'Hello Arduino\n'
    # str型をbytes型に変換
    buf = bytes(hello_str,'utf-8')
    con.write(buf)
    time.sleep(1)
    while True:
        con.write(bytes('led_on\n','utf-8'))
        time.sleep(1)
        con.write(bytes('led_off\n','utf-8'))
        time.sleep(1)

if __name__ == '__main__':
    main()

