import pyautogui as pag
import time

def startup():
    pag.write('cash 100000')
    pag.write('reformprogress 10000')
    pag.write('leader 9 9 9 9 9')
    pag.write('leader 9 9 9 9 9')
    pag.write('dip 300')
    pag.write('navy_tradition 2000')


print('Welcome to eu4 startup.')
print('You have 10 seconds.')
time.sleep(10)
startup()