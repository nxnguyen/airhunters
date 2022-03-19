import csv
import random

import pyautogui
import time

import pyperclip

from modules.captcha_warning import captcha_warning, captcha_plus_solver
from modules.telegram_jobs import TelegramController
from modules.user_model import MyUser
from ultis.mouse_keyboard_automation import keyboard_type_job, tweeter_quote_jobs

import subprocess
from modules.chrome_jobs import ChromeController

retweet_Link = ''

def findQuoteBtnFunc():
    print('findQuoteBtnFunc')
    # pyautogui.moveTo(1341, 306, 0.1)
    # pyautogui.scroll(-200)
    pass


def quoteTweet(user: MyUser, userList):
    tweeter_quote_jobs()

    # keyboard_type_job(
    #     'Excellent and great projects sir. I am impressed with this project, hopefully with this event the community and especially this coin will achieve success.')
    #
    # pyautogui.typewrite(["enter"])
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

    # keyboard_type_job('@' + userList[id1].twitterId)
    # pyautogui.typewrite(["enter"])
    # keyboard_type_job('@' + userList[id2].twitterId)
    # pyautogui.typewrite(["enter"])
    # keyboard_type_job('@' + userList[id3].twitterId)
    # pyautogui.typewrite(["enter"])
    # pyautogui.typewrite(["enter"])

    keyboard_type_job('#MCG')
    pyautogui.typewrite(["enter"])

    pass


def step1(user: MyUser, userList):
    global retweet_Link
    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    chromeCtrl.tweeter_follow('https://twitter.com/MagicCardGame_')
    time.sleep(1)

    chromeCtrl.tweeter_follow('https://twitter.com/AirdropStario')

    chromeCtrl.tweeter_retweet('https://twitter.com/AirdropStario/status/1452021537792528387', 3)
    retweet_Link = chromeCtrl.tweeter_quote_tweet(
        'https://twitter.com/MagicCardGame_/status/1452377436155310081', findQuoteBtnFunc,
        quoteTweet, userList)
    print(retweet_Link)


    # =======================================================

    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()
    teleCtrl.telegram_join_channel('https://t.me/magiccardNFT')
    teleCtrl.telegram_join_channel('https://t.me/magiccardNFTann')
    teleCtrl.telegram_note_down(retweet_Link)
    pass


def step2(user: MyUser, userList):
    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()

    teleCtrl.telegram_join_channel('https://t.me/MagicCardGameAirdropBot?start=2069310083')

    teleCtrl.telegram_press_level(1)
    time.sleep(3)
    teleCtrl.telegram_press_level(2)
    time.sleep(3)
    teleCtrl.telegram_press_level(1)
    captcha_warning()


    teleCtrl.telegram_press_level(2)
    time.sleep(1)
    keyboard_type_job(user.mail)
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    keyboard_type_job(user.bscWallet)
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    keyboard_type_job(user.twitterProfileLink)
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    keyboard_type_job(retweet_Link)
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    teleCtrl.telegram_press_level(2)
    time.sleep(3)
    teleCtrl.telegram_press_level(2)
    pass


def start_script(userList):
    pyautogui.click(216, 145)
    time.sleep(1)
    # for i in range(9, 11):
    #     userId = i
    for i in range(1, 2):
        userId = 10

        user: MyUser = userList[userId - 1]

        print(user.id)


        step1(user, userList)
        step2(user, userList)


userList = []
with open("C://Users//nxngu//Dropbox//AirdropProjects//user_db.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        userList.append(MyUser())
        userList[len(userList) - 1].init_by_row(row)
start_script(userList)