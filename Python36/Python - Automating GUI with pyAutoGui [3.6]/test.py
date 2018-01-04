import pyautogui
# how to find the position mouse?
a = pyautogui.position()
print(a)
pyautogui.rightClick(74, 124)
pyautogui.click(217, 139)
pyautogui.moveTo(471, 138)
pyautogui.click(471, 138)
pyautogui.typewrite("ambig1")
pyautogui.typewrite(["enter"])
