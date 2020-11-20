from microbit import i2c
# the following imports are for the example code at the end of the file
from microbit import *
from math import pow, acos, degrees, sqrt, atan


class KitronikServoBoard:
    BOARD_1 = 0x6A

    # the prescale register address
    PRESCALE_REG = 0xFE

    # The mode 1 register address
    MODE_1_REG = 0x00

    # If you wanted to write some code that stepped through
    # the servos then this is the Base and size to do that
    SERVO_1_REG_BASE = 0x08
    SERVO_REG_DISTANCE = 4

    # To get the PWM pulses to the correct size and zero
    # offset these are the default numbers.
    SERVO_MULTIPLIER = 226
    SERVO_ZERO_OFFSET = 0x66

    # a flag to allow us to initialise without explicitly
    # calling the secret incantation
    INITALISED = False

    class Servos:
        # nice big list of servos to use.
        # These represent register offsets in the PCA9865
        SERVO_1 = 0x08
        SERVO_2 = 0x0C
        SERVO_3 = 0x10
        SERVO_4 = 0x14

    # Trim the servo pulses. These are here for advanced users,
    # It appears that servos I've tested are actually expecting
    # 0.5 - 2.5mS pulses, not the widely reported 1-2mS.
    # that equates to multiplier of 226, and offset of 0x66
    # a better trim function that does the maths for the end
    # user could be written, the basics are here for reference

    def trim_servo_multiplier(self, trim_value):
        if trim_value < 113:
            self.SERVO_MULTIPLIER = 113

        else:
            if trim_value > 226:
                self.SERVO_MULTIPLIER = 226
            else:
                self.SERVO_MULTIPLIER = trim_value

    def trim_servo_zero_offset(self, trim_value):
        if trim_value < 0x66:
            self.SERVO_ZERO_OFFSET = 0x66
        else:
            if (trim_value > 0xCC):
                self.SERVO_ZERO_OFFSET = 0xCC
            else:
                self.SERVO_ZERO_OFFSET = trim_value

    def _secret_incantation(self):
        # This secret incantation sets up the PCA9865 I2C driver chip to
        # be running at 50Hz pulse repetition, and then sets the 16 output
        # registers to 1.5mS - centre travel on the servos.
        # It should not need to be called directly be a user -
        # the first servo write will call it.

        buf = bytearray(2)
        # Should really do a soft reset of the I2C chip here
        # First set the prescaler to 50 hz
        buf[0] = self.PRESCALE_REG
        buf[1] = 0x85
        i2c.write(self.BOARD_1, buf, False)
        # Block write via the all leds register to set all of them to 90 deg
        buf[0] = 0xFA
        buf[1] = 0x00
        i2c.write(self.BOARD_1, buf, False)
        buf[0] = 0xFB
        buf[1] = 0x00
        i2c.write(self.BOARD_1, buf, False)
        buf[0] = 0xFC
        buf[1] = 0x66
        i2c.write(self.BOARD_1, buf, False)
        buf[0] = 0xFD
        buf[1] = 0x00
        i2c.write(self.BOARD_1, buf, False)
        # Set the mode 1 register to come out of sleep
        buf[0] = self.MODE_1_REG
        buf[1] = 0x01
        i2c.write(self.BOARD_1, buf, False)
        # set the initalised flag so we dont come in here again automatically
        self.INITALISED = True

    def servo_write(self, Servo: Servos, degrees):
        # sets the requested servo to the reguested angle.
        # if the PCA has not yet been setup calls the initialisation routine
        # @param Servo Which servo to set
        # @param degrees the angle to set the servo to
        if self.INITALISED is False:
            self._secret_incantation(self)
        buf = bytearray(2)
        HighByte = False
        PWMVal = degrees + 180
        #deg100 = degrees * 100
        #PWMVal100 = deg100 * self.SERVO_MULTIPLIER
        #PWMVal = PWMVal100 / 10000
        #PWMVal = PWMVal + self.SERVO_ZERO_OFFSET
        #print(self.SERVO_ZERO_OFFSET)
        #print(PWMVal)
        if (PWMVal > 0xFF):
            HighByte = True
        buf[0] = Servo
        buf[1] = int(PWMVal)
        i2c.write(self.BOARD_1, buf, False)
        if (HighByte):
            buf[0] = Servo + 1
            buf[1] = 0x01
        else:
            buf[0] = Servo + 1
            buf[1] = 0x00
        i2c.write(self.BOARD_1, buf, False)


def parse_command(command):
    g = -1
    i = -1
    j = -1
    k = -1
    xl = -1
    yl = -1
    out = "G0"

    if command != "\r\n":
        out = command[:-2].split(" ")

    print(out)

    for e in out:
        pre = e[0]
        val = e[1:]
        if pre == 'G':
            g = val
        if pre == 'I':
            i = val
        if pre == 'J':
            j = val
        if pre == 'K':
            k = val
        if pre == 'X':
            xl = val
        if pre == 'Y':
            yl = val

    return g, i, j, k, xl,yl

def collect_command():
    command = b''

    while True:
        while not uart.any():
            pass

        c = uart.read()
        command += c

        uart.write(bytes(c))

        command_str = str(command, 'UTF-8')

        if command_str.startswith("\r\n"):
            command = b"G1\r\n"
            return command

        if command_str.endswith("\r\n"):
            return command

def xy2alphabeta(x0, y0):

    l=80.0
    m=80.0
    z=sqrt(pow(x0,2) + pow(y0,2))

    abc = degrees(acos((-pow(l,2) + pow(m,2) + pow(z,2))/(2*m*z)))
    bac = degrees(acos((-pow(m,2) + pow(l,2) + pow(z,2))/(2*l*z)))
    bad = degrees(atan(y0/x0))
    acb = 180.0 - abc - bac

    beta0 = 180.0 - bac - bad
    alpha0 = 180.0 - bac - bad - acb

    return alpha0, beta0

def alphabeta2JK(alpha1, beta1):
#    k_float = - 4.64 * alpha1 + 438
#    j_float = 4.05 * beta1 - 321.2
    k_float = - 1.7 * alpha1 + 218.35
    j_float = 1.48 * beta1 - 50.476
    j1 = int(j_float)
    k1 = int(k_float)
    return j1, k1


uart.init(baudrate=115200)

uart.write("robot>")

while not uart.any():
  pass

theServoBoard = KitronikServoBoard

theServoBoard.servo_write(theServoBoard,
                          KitronikServoBoard.Servos.SERVO_1,
                          25)
theServoBoard.servo_write(theServoBoard,
                          KitronikServoBoard.Servos.SERVO_2,
                          105)
theServoBoard.servo_write(theServoBoard,
                          KitronikServoBoard.Servos.SERVO_3,
                          95)

x_glob = 40
y_glob = 0

while True:
    command = collect_command()
    command_str = str(command, 'UTF-8')

    g, i, j, k, x, y = parse_command(command_str)

    # uart.write(bytes("["+command_str+"]robot>", "utf8"))
    uart.write(bytes("robot>", "utf8"))

    if command == b".\r\n":
        uart.write(bytes("stop", "utf8"))
        break

    if (x != -1) or (y != -1):
        if x != -1:
            x_glob = x
        if y != -1:
            y_glob = y

        alpha, beta = xy2alphabeta(float(x_glob), float(y_glob))
        i = -1
        j, k = alphabeta2JK(alpha, beta )

    if i != -1:
        theServoBoard.servo_write(theServoBoard,
                                KitronikServoBoard.Servos.SERVO_1,
                                int(i))
    if j != -1:
        theServoBoard.servo_write(theServoBoard,
                                KitronikServoBoard.Servos.SERVO_2,
                                int(j))
    if k != -1:
        theServoBoard.servo_write(theServoBoard,
                                KitronikServoBoard.Servos.SERVO_3,
                                int(k))