import pyautogui
import time
from modules.captcha_warning import captcha_warning
from modules.telegram_jobs import TelegramController
from ultis.mouse_keyboard_automation import keyboard_type_job

import subprocess
from modules.chrome_jobs import ChromeController

def start_script(userList):
    for user in range(2, 3):
        userId = 2
        user = userList[userId - 1]

        print(user.id)

        pyautogui.click(216, 145)
        time.sleep(1)


        chromeCtrl = ChromeController(user)
        chromeCtrl.chrome_open()
        chromeCtrl.go_to_url('https://sweepwidget.com/view/37174-9ys72nr1')

        time.sleep(3)
        pyautogui.click(1002, 1786)

        keyboard_type_job(user.name)
        pyautogui.typewrite(["tab"])
        keyboard_type_job(user.mail)
        pyautogui.typewrite(["enter"])



