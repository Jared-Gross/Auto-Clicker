import pyautogui as py
import threading, time
import keyboard as kb
from pynput.mouse import Button, Controller
from colorama import init
from termcolor import colored
init()
isOn = False
mousePos = 0
delay = ''
button = Button.left
mouse = Controller()
def keyPressed():
    while True:
        if kb.is_pressed('q'): 
            global isOn
            isOn = not isOn
            continue
def click():
    while True:
        global mousePos
        if kb.is_pressed('q'): mousePos = py.position()
        else: 
            if isOn: 
                mouse.click(button)
                time.sleep(float(delay))
def move_mouse():
    while True:
        if isOn: py.moveTo(mousePos)
slow = colored("S" + "\u0332",'white') + colored('low: 0.01','white')
recommended = colored("R" + "\u0332",'green') + colored('ecommended: 0.001','green')
fast = colored("F" + "\u0332",'yellow') + colored('ast: 0.0001','yellow')
insane = colored("I" + "\u0332",'red') + colored('NSANE: 0.0001','red')
print(f'{slow}\n{recommended}\n{fast}\n{insane}', colored('\n\nInput a delay:','magenta'))
delay = input()
if delay.lower() == 'slow' or delay.lower() == 's': delay = 0.01
elif delay.lower() == 'recommended' or delay.lower() == 'r': delay = 0.001
elif delay.lower() == 'fast' or delay.lower() == 'f': delay = 0.0001
elif delay.lower() == 'insane' or delay.lower() == 'i': delay = 0.00001
elif '0.' in delay: pass
else:
    print(colored(f'"{delay}"','cyan'), colored('is not a valid delay.\nMust be smaller than','red'),colored('1','cyan'))
    time.sleep(2)
    quit()
print(colored('Starting...','yellow'))
threading.Thread(target=move_mouse).start()
threading.Thread(target=click).start()
threading.Thread(target=keyPressed).start()
time.sleep(15)
print(colored("Ready!",'green'), colored("\nPress",'magenta'), colored('"q"','cyan'), colored("to toggle",'magenta'), colored('on','blue'), colored('and', 'magenta'), colored('off','blue'), colored("\nRunning with a delay of:",'magenta'),colored(str(delay),'cyan'))
