import random

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
    pyautogui.scroll(-400)
    pass


def quoteTweet(user: MyUser, userList):
    # keyboard_type_job(
    #     'I like surprises i really like the strategy of the team this project is a rare gem glad i had played this game more power.')
    # pyautogui.typewrite(["enter"])

    id1, id2, id3, id4 = random.sample(range(0, 10), 4)
    #
    # print(id1)
    # print(id2)
    # print(id3)
    # print(id4)

    if id1 == user.id - 1:
        id1 = id4
    if id2 == user.id - 1:
        id2 = id4
    if id3 == user.id - 1:
        id3 = id4

    # print(id1)
    # print(id2)
    # print(id3)
    # print(id4)

    keyboard_type_job('@' + userList[id1].twitterId)
    # pyautogui.typewrite(["enter"])
    pyautogui.typewrite(["enter"])
    keyboard_type_job('@' + userList[id2].twitterId)
    pyautogui.typewrite(["enter"])
    # pyautogui.typewrite(["enter"])
    keyboard_type_job('@' + userList[id3].twitterId)
    pyautogui.typewrite(["enter"])
    pyautogui.typewrite(["enter"])
    pass


def step1(user: MyUser, userList):
    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    chromeCtrl.tweeter_follow('https://twitter.com/Btrips_Project')
    time.sleep(1)
    retweet_Link = chromeCtrl.tweeter_quote_tweet(
        'https://twitter.com/Btrips_Project/status/1450821022052061195', findQuoteBtnFunc,
        quoteTweet, userList)
    print(retweet_Link)

    # =======================================================

    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()
    teleCtrl.telegram_join_channel('https://t.me/btripsglobalchat')
    teleCtrl.telegram_join_channel('https://t.me/BTRIPSOFFICIAL')
    pass


def step2(user: MyUser, userList):
    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()

    teleCtrl.telegram_join_channel('http://t.me/BTRIPSAirdropBot')

    time.sleep(3)
    pyautogui.click(1606, 1777)
    time.sleep(3)
    pyautogui.click(1606, 1777)

    # captcha_warning()

    time.sleep(3)
    pyautogui.click(1606, 1777)

    time.sleep(3)
    pyautogui.click(1606, 1777)

    time.sleep(2)


    keyboard_type_job('@' + user.twitterId)
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    pyautogui.click(1563, 1584)

    keyboard_type_job(user.etherWallet)
    pyautogui.typewrite(["enter"])
    pass


def start_script(userList):
    # for i in range(1, 2):
    #     userId = 5
    for i in range(6, 11):
        userId = i

        user: MyUser = userList[userId - 1]

        print(user.id)

        pyautogui.click(216, 145)
        time.sleep(1)

        # step1(user, userList)
        step2(user, userList)


