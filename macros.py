import time
import pyautogui as auto

screenWidth, screenWeigth = auto.size()

time.sleep(3)


cont = 1
while cont == 1:

    auto.click(auto.position())
    time.sleep(0.5)

