# a2r.py
import serial
import time

def main():
    con = serial.Serial('/dev/ttyACM0',9600)
    time.sleep(2)
    print (con.portstr)
    while True:
        con_str = con.readline()
        print(con_str)

if __name__ == '__main__':
    main()
