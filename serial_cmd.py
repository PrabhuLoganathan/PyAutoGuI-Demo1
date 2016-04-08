import serial

class Serial():
    def __init__(self):

        #try:
        self.ser = serial.Serial('COM7')
        #except SerialException:
        #self.ser = serial.Serial('/dev/ttyS0')

        try:
            self.ser.open()
        except serial.SerialException, e:
            print e

    def write(self):
        while True:
            ch = raw_input("ch: ")
            self.ser.write(ch)

            if ch == '7':
                break
        self.ser.close()

if __name__ == '__main__':
    obj = Serial()
    obj.write()
