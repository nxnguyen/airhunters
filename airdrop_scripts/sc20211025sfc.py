import pyautogui
import time

import pyperclip

from modules.captcha_warning import captcha_warning, captcha_plus_solver
from modules.telegram_jobs import TelegramController
from modules.user_model import MyUser
from ultis.mouse_keyboard_automation import keyboard_type_job

import subprocess
from modules.chrome_jobs import ChromeController


def findQuoteBtnFunc():
    print('findQuoteBtnFunc')
    pyautogui.moveTo(1341, 306, 0.1)
    pyautogui.scroll(-200)
    pass


def quoteTweet():
    keyboard_type_job(
        'I like surprises i really like the strategy of the team this project is a rare gem glad i had played this game more power.')
    pyautogui.typewrite(["enter"])
    keyboard_type_job('@GuenShun')
    pyautogui.typewrite(["enter"])
    pyautogui.typewrite(["enter"])
    keyboard_type_job('@GuenShun')
    pyautogui.typewrite(["enter"])
    pyautogui.typewrite(["enter"])
    keyboard_type_job('@GuenShun')
    pyautogui.typewrite(["enter"])
    pyautogui.typewrite(["enter"])
    pass


def step1(user: MyUser):
    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    chromeCtrl.tweeter_follow('https://twitter.com/SafeCap_Token')
    time.sleep(1)
    chromeCtrl.go_to_url('https://twitter.com/SafeCap_Token/status/1452156143732604930')
    pyautogui.press('down')
    pyautogui.press('down')
    time.sleep(1)

    pyautogui.click(1167, 1746)

    time.sleep(1)
    pyautogui.click(1086, 1662)

    # =======================================================

    # teleCtrl = TelegramController(user)
    # teleCtrl.telegram_open()
    # teleCtrl.telegram_join_channel('https://t.me/Safecap_Official')
    # teleCtrl.telegram_join_channel('https://t.me/SafeCap_Token')
    pass


def step2(user: MyUser):
    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()

    teleCtrl.telegram_join_channel('https://t.me/SafeCapAirdropBot?start=2069310083')

    time.sleep(2)
    pyautogui.click(1602, 1787)

    time.sleep(2)
    pyautogui.click(1559, 1679)

    pyautogui.rightClick(1549, 1465)
    time.sleep(1)
    pyautogui.click(1654, 1147)
    time.sleep(1)

    answer = captcha_plus_solver(pyperclip.paste())

    pyautogui.click(1436, 1772)
    keyboard_type_job(answer)
    time.sleep(3)
    pyautogui.typewrite(["enter"])

    # captcha_warning()

    time.sleep(3)
    pyautogui.click(1531, 1664)
    time.sleep(3)
    pyautogui.click(1531, 1664)

    pyautogui.click(1487, 1781)
    time.sleep(1)

    keyboard_type_job('@' + user.twitterId)
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    pyautogui.click(1563, 1584)

    keyboard_type_job(user.bscWallet)
    pyautogui.typewrite(["enter"])
    pass


def start_script(userList):
    for i in range(9, 11):
        userId = i

        user: MyUser = userList[userId - 1]

        print(user.id)

        pyautogui.click(216, 145)
        time.sleep(1)

        # step1(user)
        step2(user)


