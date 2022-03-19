import csv
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
    pyautogui.scroll(-200)
    pass


def quoteTweet(user: MyUser, userList):
    keyboard_type_job(
        'Excellent and great projects sir. I am impressed with this project, hopefully with this event the community and especially this coin will achieve success.')

    pyautogui.typewrite(["enter"])
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

    keyboard_type_job('#XPAY #BNB #Dxsale #Binance')
    pyautogui.typewrite(["enter"])

    pass


def step1(user: MyUser, userList):
    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    chromeCtrl.tweeter_follow('https://twitter.com/walletpay_app')
    chromeCtrl.tweeter_follow('https://twitter.com/AirdropStario')
    chromeCtrl.tweeter_retweet('https://twitter.com/AirdropStario/status/1452342835164946450', 3)

    time.sleep(1)



    retweet_Link = chromeCtrl.tweeter_quote_tweet(
        'https://twitter.com/walletpay_app/status/1451739455128231937', findQuoteBtnFunc,
        quoteTweet, userList)
    print(retweet_Link)

    chromeCtrl.go_to_url('https://www.reddit.com/r/walletpay/')

    # =======================================================

    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()
    teleCtrl.telegram_join_channel('https://t.me/WalletPayOfficial')
    teleCtrl.telegram_join_channel('https://t.me/walletpayannouncements')
    teleCtrl.telegram_join_channel('https://t.me/Airdrop')
    teleCtrl.telegram_note_down(retweet_Link)
    pass


def step2(user: MyUser, userList):
    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()

    teleCtrl.telegram_join_channel('https://t.me/WalletPay2ndRoundAirdropBot?start=2069310083')

    pyautogui.click(1605, 1780)
    time.sleep(3)
    pyautogui.click(1615, 1675)
    time.sleep(3)
    pyautogui.click(1588, 1771)
    captcha_warning()

    pyautogui.click(1591, 1671)

    keyboard_type_job(user.mail)
    pyautogui.typewrite(["enter"])

    time.sleep(3)
    keyboard_type_job(user.bscWallet)
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    keyboard_type_job(user.twitterProfileLink)
    pyautogui.typewrite(["enter"])
    captcha_warning()

    pyautogui.click(1591, 1671)
    time.sleep(3)
    pyautogui.click(1591, 1671)
    keyboard_type_job(user.redditProfileLink)
    pyautogui.typewrite(["enter"])

    time.sleep(3)
    pyautogui.click(1646, 1677)
    time.sleep(3)
    pyautogui.click(1646, 1677)

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


        # step1(user, userList)
        step2(user, userList)


userList = []
with open("C://Users//nxngu//Dropbox//AirdropProjects//user_db.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        userList.append(MyUser())
        userList[len(userList) - 1].init_by_row(row)
start_script(userList)