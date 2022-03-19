import pyautogui
from playsound import playsound
import time
import pyperclip
import re


def captcha_warning():
    playsound('sounds/captcha.wav')
    pyautogui.alert('Complete CAPTCHA then click OK to continue')

def captcha_plus_solver(str):
    str = pyperclip.paste()
    print(str)

    map = re.findall('\d+', str)

    total = 0
    if str.find("+") != -1:
        total = int(map[0]) + int(map[1])
    else:
        total = int(map[0]) - int(map[1])
    return total