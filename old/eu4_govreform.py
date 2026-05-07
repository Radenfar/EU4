import pyautogui as pag
import time

print("You have 10 seconds.")
time.sleep(10)
while not pag.position()[1] < 50:
    pag.click()
