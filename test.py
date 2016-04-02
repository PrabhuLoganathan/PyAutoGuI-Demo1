from __future__ import print_function
import pyautogui
import sys

print('Ctrl-C to exit')

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='')
        sys.stdout.flush()
except KeyboardInterrupt:
    print('\nDone')
