from mySerial import Serial
import pyautogui as p

width, height = p.size()

def main():
    ser = Serial()

    while True:
        data = ser.read()
        if data == '7':
            print "ABORTING !!"
            break
        
        elif data == '1':
            print "Left Click"
            try:
                p.click(button = 'left')
            except Exception, e:
                print e
        elif data == '2':
            print "Right Click"
            try:
                p.click(button = 'right')
            except Exception, e:
                print e
        elif data == 'a':
            print "Left Key"
            try:
                p.moveRel(-10,0)
            except Exception,e:
                print e
        elif data == 'd':
            print "Right Key"
            try:
                p.moveRel(10,0)
            except Exception, e:
                print e
        elif data == 's':
            print "Down key"
            try:
                p.moveRel(0,10)
            except Exception,e:
                print e
        elif data == 'w':
            print "Up key"
            try:
                p.moveRel(0,-10)
            except Exception,e:
                print e
                
        else:
            print "Unknown cmd: ", data
        

if __name__ == '__main__':
    main()
