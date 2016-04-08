import serial

class Serial():
    def __init__(self):

        #try:
        self.ser = serial.Serial('COM1')
        #except SerialException:
        #self.ser = serial.Serial('/dev/ttyS0')

        try:
            self.ser.open()
        except serial.SerialException, e:
            print e

    def read(self):
        ch = self.ser.read(1)
        print ch
        if ch == '7':
            try:
                self.ser.close()
            except serial.SerialException, e:
                print e
        return ch

if __name__ == '__main__':
    print "Hello"
