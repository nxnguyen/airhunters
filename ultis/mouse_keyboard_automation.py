from random import randrange

import pyautogui
import pyperclip
import time


def keyboard_type_job(words):
    words = str(words)
    pyautogui.typewrite(words, interval=0.05)
    # for char in words:
    #     pyperclip.copy(char)
    #     pyautogui.hotkey('ctrl', 'v')

def tweeter_quote_jobs():
    quoteId = randrange(7)

    if quoteId == 0:
        keyboard_type_job('Nice project, as big and powerful as a giant.')
        pyautogui.typewrite(["enter"])
        keyboard_type_job('hope it grows fast with the biggest followers in the world')
    elif quoteId == 1:
        keyboard_type_job('Very good project')
    elif quoteId == 2:
        keyboard_type_job('Nice project')
    elif quoteId == 3:
        keyboard_type_job('Good project')
    elif quoteId == 4:
        keyboard_type_job('This project looks really interesting. I am interested, and I will support this project until it works according to the plan that has been set')
    elif quoteId == 5:
        keyboard_type_job('It is a good project. Hope it will go a long way in the future. Thanks team.')
    elif quoteId == 6:
        keyboard_type_job('This is an amazing project, great devs/love the community growth. Lets us hope to see this token skyrocket above and beyond.')

    pyautogui.typewrite(["enter"])
