import pyautogui as py
import threading, time, platform, os
import keyboard as kb
from pynput.mouse import Button, Controller
from colorama import init
from termcolor import colored
# pip install termcolor, colorama, keyboard, pyautogui, pynput
init()
if platform.system() == 'Windows': clear = lambda: os.system('cls')
elif platform.system() == 'Linux': clear = lambda: os.system('clear')
isOn = False
threadsRunning = False
mousePos = []
delay = ''
button = Button.left
mouse = Controller()
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = colored(("{0:." + str(decimals) + "f}%").format(100 * (iteration / float(total))),'cyan')
    filledLength = int(length * iteration // total)
    bar = colored('|' + fill * filledLength + '-' * (length - filledLength) + '|','green')
    print((f'\r{prefix} {bar} {percent} {suffix}'), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
def move_mouse():
    while True:
        if isOn: py.moveTo(mousePos)
        time.sleep(0.01)
def running():
    while True:
        if kb.is_pressed('q'):
            global isOn, mousePos
            mousePos = py.position()
            isOn = not isOn
        elif kb.is_pressed('e'):
            isOn = False
            get_delay()
        else:
            if isOn:
                mouse.click(button)
                time.sleep(float(delay))
        time.sleep(0.001)
def get_delay():
    global threadsRunning, delay
    clear()
    recommended = colored("R" + "\u0332",'green') + colored('ecommended: 0.01','green')
    fast = colored("F" + "\u0332",'yellow') + colored('ast: 0.001','yellow')
    insane = colored("I" + "\u0332",'red') + colored('NSANE: 0.0001','red')
    print(f'{recommended}\n{fast}\n{insane}', colored('\n\nInput a delay:','magenta'))
    delay = input()
    if delay.lower() == 'recommended' or delay.lower() == 'r': delay = 0.01
    elif delay.lower() == 'fast' or delay.lower() == 'f': delay = 0.001
    elif delay.lower() == 'insane' or delay.lower() == 'i': delay = 0.0001
    elif '0.' in delay: pass
    else:
        print(colored(f'"{delay}"','cyan'), colored('is not a valid delay.\nMust be smaller than','red'),colored('1','cyan'))
        time.sleep(1)
        get_delay()
    if not threadsRunning:
        threading.Thread(target=running).start()
        threading.Thread(target=move_mouse).start()
        items = list(range(0, 70))
        threadsRunning = True
    else:
        items = list(range(0,1))
    l = len(items)
    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = colored('Starting:','yellow'), suffix = colored('Complete','cyan'), length = 40)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = colored('Starting:','yellow'), suffix = colored('Complete','cyan'), length = 40)
    clear()
    print(colored("Ready!",'green'))
    time.sleep(1)
    clear()
    print(colored("Press:",'magenta'), colored('"q"','cyan'), colored("to toggle",'magenta'), colored('on','blue'), colored('and', 'magenta'), colored('off','blue'))
    print(colored('Press:','magenta'),colored('"e"','cyan'), colored('to change delay.','magenta'))
    print(colored("Delay set to:",'magenta'),colored(str(delay),'cyan'))
get_delay()
