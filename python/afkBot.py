import pyautogui
import random
import time

curr_cords = pyautogui.position()
afk_counter = 0
while True:
    if pyautogui.position() == curr_cords:
        afk_counter += 1
    else:
        afk_counter = 0
        curr_cords = pyautogui.position()
        
    if afk_counter > 5:
        x = random.randint(1080 - 500, 1920 - 500)
        y = random.randint(1080 - 500, 1920 - 500)
        pyautogui.moveTo(x, y, 0.5)
        curr_cords = pyautogui.position()
    print(f'AFK counter: {afk_counter}')    
    time.sleep(2)
