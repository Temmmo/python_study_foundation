import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print(pyautogui.size())
width, height = pyautogui.size()
for i in range(100000000):
    pyautogui.moveTo(100, 100, duration=10)
    pyautogui.moveTo(100, 100, duration=10)
    pyautogui.moveTo(100, 100, duration=10)

for i in range(1):
    pyautogui.moveRel(200, 0, duration=0.25)
    pyautogui.moveRel(0, 200, duration=0.25)
    pyautogui.moveRel(-200, 0, duration=0.25)
    pyautogui.moveRel(0, -200, duration=0.25)

print(pyautogui.position())
