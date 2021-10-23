import pyautogui
import pyperclip
import time


def keyboard_type_job(words):
    pyautogui.typewrite(words, interval=0.05)
    # for char in words:
    #     pyperclip.copy(char)
    #     pyautogui.hotkey('ctrl', 'v')
