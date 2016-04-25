import serial

class Serial():
    port = 0
    def __init__(self):

        try:
            self.ser = serial.Serial(self.port)
        except SerialException:
            print e

        try:
            self.ser.open()
        except serial.SerialException, e:
            print e

    def open(self):
        try:
            self.ser.close()
            self.ser = serial.Serial(self.port)
        except serial.SerialException, e:
            print e
        
    def read(self):
        self.open()
        try:
            ch = self.ser.read(1)
        except serial.SerialException, e:
            ch = '0'
            print e

        if ch == '7':
            try:
                self.ser.close()
            except serial.SerialException, e:
                print e
        return ch

if __name__ == '__main__':
    print "Hello"
