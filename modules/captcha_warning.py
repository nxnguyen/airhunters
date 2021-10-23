import pyautogui
from playsound import playsound
import time


def captcha_warning():
    playsound('sounds/captcha.wav')
    pyautogui.alert('Complete CAPTCHA then click OK to continue')
