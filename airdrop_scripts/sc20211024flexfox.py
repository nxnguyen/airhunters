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
    keyboard_type_job('I like surprises i really like the strategy of the team this project is a rare gem glad i had played this game more power.')
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

def start_script(userList):
    for i in range(2, 9):
        userId = i
    # for user in range(2, 3):
    #     userId = 1

    #     user = userList[userId - 1]
    #
    #     print(user.id)
    #
    #
    #     chromeCtrl = ChromeController(user)
    #     chromeCtrl.chrome_open()
    #     chromeCtrl.tweeter_follow('https://twitter.com/FlexFoxNFT')
    #     chromeCtrl.discord_join_invite('https://discord.gg/flexfox')
    #
    #     time.sleep(5)
    #     pyautogui.click(993, 1440)
        pass

    #============================================================
    for i in range(4, 8):
        userId = i
    # for user in range(2, 3):
        # userId = 3
        user = userList[userId - 1]

        print(user.id)


        teleCtrl = TelegramController(user)
        teleCtrl.telegram_open()

        teleCtrl.telegram_join_channel('https://t.me/FlexFox_Bot?start=r04719220511')

        time.sleep(1)
        pyautogui.click(1589, 1770)

        time.sleep(1)
        pyautogui.click(1540, 1679)

        time.sleep(1)
        keyboard_type_job(user.twitterProfileLink)

        pyautogui.typewrite(["enter"])
        time.sleep(1)
        keyboard_type_job(user.discordId)

        pyautogui.typewrite(["enter"])
        time.sleep(1)
        keyboard_type_job(user.bscWallet)

        pyautogui.typewrite(["enter"])
        time.sleep(1)
        time.sleep(1)
        pass

