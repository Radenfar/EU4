import pyautogui as pag
import time

def command(command: str):
    pag.write(command)
    time.sleep(0.5)

def startup(cash: int = 100000, leaders: int = 2):
    command(f'cash {cash}')
    command('manpower 30')
    command('reformprogress 10000')
    for _ in range(leaders):
        command('leader 9 9 9 9 9')
    command('dip 300')
    command('navy_tradition 20000')


if __name__ == "__main__":
    CASH: int = 100000
    LEADERS: int = 2
    print('Welcome to eu4 startup.')
    print('You have 5 seconds.')
    time.sleep(5)
    startup(CASH, LEADERS)