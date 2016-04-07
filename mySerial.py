import serial

class Serial():
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyS0')

        try:
            self.ser.open()
        except serial.SerialException, e:
            print e
        
        print self.ser.isOpen()

    def read(self):
        ch = self.ser.read()

        if ch == '7':
            try:
                self.ser.close()
            except serial.SerialException, e:
                print e
        return ch

if __name__ == '__main__':
    print "Hello"
