print('hello world')

import pyautogui
import time
from modules.captcha_warning import captcha_warning
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
    chromeCtrl = ChromeController(userList[0])

    stringRun = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --profile-directory="Default" --start-maximized'
    subprocess.Popen(
        r'' + stringRun,
        stderr=subprocess.PIPE)
    time.sleep(3)

    chromeCtrl.discord_join_invite('https://discord.com/invite/qWh4FrEGHD')

    # chromeCtrl.tweeter_follow('https://twitter.com/BscProjectOrg')
    # chromeCtrl.tweeter_follow('https://twitter.com/BinanceChain')
    # chromeCtrl.tweeter_follow('https://twitter.com/DeriProtocol')
    # chromeCtrl.tweeter_follow('https://twitter.com/KineProtocol')
    # chromeCtrl.tweeter_follow('https://twitter.com/MonteCarloDEX')

    retweet_Link = chromeCtrl.tweeter_quote_tweet('https://twitter.com/BinanceChain/status/1450831673931747332',findQuoteBtnFunc,
                                                  quoteTweet)
    print(retweet_Link)


    # chromeCtrl.go_to_web_tele()
    # chromeCtrl.tele_join_channel('@faraland_io')
    # chromeCtrl.tele_join_channel('https://t.me/huobiglobalpakistan'])
    # captcha_warning()
    chromeCtrl.chrome_close()

    # for user in userList:
    #     print('User ' + str(user.num) + ' ====================================')
    #     chromeCtrl = ChromeController(user)
    #     chromeCtrl.chrome_open()
    #     chromeCtrl.go_to_web_tele()
    #     chromeCtrl.tele_join_multi_channels(['@faraland_io', 'https://t.me/huobiglobalpakistan'])
    #     # captcha_warning(6)
    #     chromeCtrl.chrome_close()