import pyautogui, sys
import pygetwindow as gw 

win = gw.getWindowsWithTitle('Command Prompt')[0]
win.resizeTo(400, 200)
win.moveTo(10,10) 

print('Press Ctrl-C to quit.')
try:
    while True:
        win.activate()
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
