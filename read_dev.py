import serial
import time
ser=serial.Serial('/dev/ttyACM0',baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
print(ser.name)

ser.write(b'I')
#ser.flush()
#time.sleep(1)
ser.write(b'8')
#ser.flush()
#time.sleep(1)
ser.write(b'0')
#ser.flush()
#time.sleep(2)

ser.write(b'\r')
#ser.flush()
ser.write(b'\n')
#ser.flush()

readedText = ser.readline()
print(readedText)

readedText = ser.readline()
print(readedText)


ser.close()
