import pyautogui, time
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# get screen size and store in variables
width, height = pyautogui.size()
print(width, height)

# move mouse to absolute position
def moveto():
    for i in range(3):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)

# move mouse from relative position
def moverel():
    for i in range(3):
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)

# get mouse current position
print(pyautogui.position())