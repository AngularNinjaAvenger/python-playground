import pyautogui

x = pyautogui

x.click(512,767)
x.moveTo(513,689,duration = 10)
x.click()
# # 
x.keyDown('win')
x.press('up')
x.keyUp('win')
x.hotkey('win','up')
x.click(72,128,duration=10)
x.click(660,128,duration=10)
x.keyDown('ctrl')
x.press('a')
x.keyUp('ctrl')
x.hotkey('ctrl','a')
x.rightClick(None,268)
x.moveTo(764,378)
x.click()