import pyautogui
import time
from modules.captcha_warning import captcha_warning
from modules.telegram_jobs import TelegramController
from ultis.mouse_keyboard_automation import keyboard_type_job

import subprocess
from modules.chrome_jobs import ChromeController

def findQuoteBtnFunc():
    print('findQuoteBtnFunc')
    pyautogui.moveTo(1341, 306, 0.1)
    pyautogui.scroll(-200)
    pass

def quoteTweet():
    keyboard_type_job('#okewar #p2e')
    # pyautogui.typewrite(["enter"])
    pass

def start_script(userList):
    for user in range(2, 3):
        userId = 8
        user = userList[userId - 1]

        print(user.id)

        pyautogui.click(216, 145)
        time.sleep(1)

        chromeCtrl = ChromeController(user)
        chromeCtrl.chrome_open()

        retweet_link = chromeCtrl.tweeter_quote_tweet('https://twitter.com/OkewarBSC/status/1451508044353835009?s=20',
                                                      findQuoteBtnFunc,
                                                      quoteTweet)
        print(retweet_link)

        teleCtrl = TelegramController(user)
        teleCtrl.telegram_open()
        teleCtrl.telegram_join_channel('https://t.me/okewarchat')

        pyautogui.click(194, 98)
        time.sleep(1)
        pyautogui.click(427, 756)
        time.sleep(1)
        pyautogui.click(1300, 519)
        time.sleep(1)
        pyautogui.click(1329, 895)
        time.sleep(1)

        keyboard_type_job(user.teleUsername)
        pyautogui.typewrite(["enter"])


        # retweet_link = 'https://twitter.com/AustinShannon16/status/1452171578582523904'

        chromeCtrl = ChromeController(user)
        chromeCtrl.chrome_open()
        chromeCtrl.go_to_url('https://docs.google.com/forms/d/e/1FAIpQLSd64keAWn1t3EyzCkehtQvbx8lh3spAwG6eiQKwJ1IRolYjbA/viewform')
        pyautogui.click(1687, 1396)

        pyautogui.click(933, 1231)
        time.sleep(1)
        pyautogui.click(1024, 1234)

        keyboard_type_job('https://twitter.com/' + user.twitterId)

        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["tab"])
        keyboard_type_job(retweet_link)

        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["tab"])
        keyboard_type_job(user.teleUsername)
        pyautogui.typewrite(["tab"])
        keyboard_type_job(user.bscWallet)





