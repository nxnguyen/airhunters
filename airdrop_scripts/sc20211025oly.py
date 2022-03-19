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
    keyboard_type_job('#Crypto #cryptocurrency #Airdrop #AirdropCrypto #CryptocurrencyAirdrop')
    pyautogui.typewrite(["enter"])
    time.sleep(1)
    pass


def step1(user: MyUser):


    # teleCtrl = TelegramController(user)
    # teleCtrl.telegram_open()
    # teleCtrl.telegram_join_channel('https://t.me/airdropo')
    # teleCtrl.telegram_join_channel('https://t.me/OfficialOlySportNews')
    # teleCtrl.telegram_join_channel('https://t.me/OlysportOfficialGroup')
    # =======================================================

    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    # chromeCtrl.tweeter_follow('https://twitter.com/oly_sport')
    # time.sleep(1)
    # chromeCtrl.tweeter_follow('https://twitter.com/cryptotownEU')
    # time.sleep(1)
    # chromeCtrl.go_to_url('https://twitter.com/CryptoTownEU/status/1452228307764797444?t=kr39QDimFWfqt9pGMZdv_w&s=19')
    retweet_Link = chromeCtrl.tweeter_quote_tweet('https://twitter.com/CryptoTownEU/status/1452228307764797444?t=kr39QDimFWfqt9pGMZdv_w&s=19',findQuoteBtnFunc,
                                                  quoteTweet)
    print(retweet_Link)
    # time.sleep(1)
    #
    # pyautogui.click(1159, 1801)
    #
    #
    # time.sleep(1)
    # pyautogui.click(1061, 1722)
    #
    # chromeCtrl.go_to_url('https://www.youtube.com/c/Airdropninja')
    # pyautogui.click(2446, 773)
    #


    pass


def step2(user: MyUser):
    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()

    teleCtrl.telegram_join_channel('https://t.me/OlySportAirdropbot?start=r08778781011')

    time.sleep(2)
    pyautogui.click(1623, 1779)
    time.sleep(2)
    pyautogui.click(1613, 1680)
    time.sleep(2)
    pyautogui.click(1613, 1680)

    # captcha_warning()
    keyboard_type_job( user.twitterProfileLink)
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    pyautogui.click(1563, 1584)

    keyboard_type_job(user.bscWallet)
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    pyautogui.click(1607, 1659)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.typewrite(["enter"])
    #https://twitter.com/AustinShannon16/status/1452341545579864065
    pass


def start_script(userList):
    for i in range(1, 2):
        userId = i
        userId = 10

        user: MyUser = userList[userId - 1]

        print(user.id)

        pyautogui.click(216, 145)
        time.sleep(1)

        step1(user)
        step2(user)

        time.sleep(10)


