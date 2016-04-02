import pyautogui as p
from datetime import datetime as dt

p.PAUSE = 1

print "Press Windows key"
p.press('winleft')

print "Type note"
p.typewrite('note')

print "Press Enter"
p.press('enter')

print "Ctrl-N -> New Note"
p.hotkey('ctrlleft', 'n')

print "Ctrl-A -> Select All"
p.hotkey('ctrlleft', 'a')

print "Press Delete"
p.press('del')

print "Type timstamp and Hello World"
p.typewrite(str(dt.now()) + ' Hello World!')
