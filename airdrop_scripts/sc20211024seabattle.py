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
    for user in range(2, 3):
        userId = 8
        user = userList[userId - 1]

        print(user.id)
        print(user.bscWallet)

        pyautogui.click(216, 145)
        time.sleep(1)


        chromeCtrl = ChromeController(user)
        chromeCtrl.chrome_open()
        chromeCtrl.tweeter_follow('https://twitter.com/SeaBattleNFT')
        time.sleep(1)
        chromeCtrl.go_to_url('https://twitter.com/SeaBattleNFT/status/1450637151515774976')

        pyautogui.click(1190, 1794)

        time.sleep(1)
        pyautogui.click(1032, 1703)


        #=======================================================

        teleCtrl = TelegramController(user)
        teleCtrl.telegram_open()
        teleCtrl.telegram_join_channel('https://t.me/airdrop6officialchannel')
        teleCtrl.telegram_join_channel('https://t.me/SeaBattleNFTGroup')
        teleCtrl.telegram_join_channel('https://t.me/SeaBattleNFTChannel')
        # teleCtrl.telegram_join_channel('https://t.me/OverlordAnn')


        teleCtrl.telegram_join_channel('https://t.me/SeaBattleAirdropBot?start=2069310083')

        time.sleep(2)
        pyautogui.click(1602, 1787)

        time.sleep(2)
        pyautogui.click(1559, 1679)
        captcha_warning()

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

