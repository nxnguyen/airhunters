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



def findQuoteBtnFunc():
    print('findQuoteBtnFunc')
    pyautogui.typewrite(["down"])
    time.sleep(1)
    pyautogui.typewrite(["down"])
    pass


def quoteTweet(user: MyUser, userList):
    tweeter_quote_jobs()

    pyautogui.typewrite(["enter"])

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

    keyboard_type_job('#CPAN #BNB #Binance')
    pyautogui.typewrite(["enter"])

    pass


def step1(user: MyUser, userList):
    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()

    chromeCtrl.discord_join_invite('https://discord.com/invite/ZUsxPc2JGR')

    chromeCtrl.go_to_url('https://twitter.com/')
    chromeCtrl.tweeter_follow('http://twitter.com/NFTCryptoPlanes')
    retweet_Link = chromeCtrl.tweeter_quote_tweet('https://twitter.com/NFTCryptoPlanes/status/1451530565765636108', findQuoteBtnFunc,
        quoteTweet, userList)
    print(retweet_Link)

    time.sleep(1)

    # =======================================================

    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()
    teleCtrl.telegram_join_channel('https://t.me/CryptoPlanes')
    teleCtrl.telegram_join_channel('https://t.me/CryptoPlanesGlobal')
    teleCtrl.telegram_join_channel('https://t.me/CryptoCityMetaverse')
    teleCtrl.telegram_note_down(retweet_Link)
    pass


def step2(user: MyUser, userList):

    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()

    teleCtrl.telegram_join_channel('https://t.me/CryptoPlanes_Airdrop_Bot?start=r03094923870')
    time.sleep(2)

    pyautogui.click(1621, 1786)

    captcha_warning()

    teleCtrl.telegram_press_level(1)
    time.sleep(3)
    teleCtrl.telegram_press_level(4)
    time.sleep(3)

    teleCtrl.telegram_press_level(2)
    time.sleep(3)


    keyboard_type_job(user.twitterProfileLink)
    pyautogui.typewrite(["enter"])
    time.sleep(3)

    keyboard_type_job(user.discordId)
    pyautogui.typewrite(["enter"])
    time.sleep(3)

    keyboard_type_job(user.bscWallet)
    pyautogui.typewrite(["enter"])
    time.sleep(3)

    pass

def start_script(userList):
    pyautogui.click(216, 145)
    time.sleep(1)
    for i in range(6, 11):
        userId = i
    # for i in range(1, 2):
    #     userId = 2

        user: MyUser = userList[userId - 1]

        print(user.id)


        # step1(user, userList)
        step2(user, userList)
        time.sleep(1)


userList = []
with open("C://Users//nxngu//Dropbox//AirdropProjects//user_db.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        userList.append(MyUser())
        userList[len(userList) - 1].init_by_row(row)
start_script(userList)