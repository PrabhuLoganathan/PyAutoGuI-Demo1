import pyautogui

button = pyautogui.locateOnScreen('cancel.png')
cords = pyautogui.center(button)
pyautogui.click(cords)
