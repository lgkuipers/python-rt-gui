import serial
import time
ser=serial.Serial('/dev/ttyACM0',baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
print(ser.name)

ser.write(b'I90\r\n')

readedText = ser.readline()
print(readedText)

readedText = ser.readline()
print(readedText)


ser.close()
