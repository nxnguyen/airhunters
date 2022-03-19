
# python main.py
# python autospy.py

# import modules.csv_reader

import csv
import time

import pyautogui

from modules.chrome_jobs import ChromeController
from modules.telegram_jobs import TelegramController
from modules.user_model import MyUser
# from airdrop_scripts.sc20211020helloworld import start_script
from airdrop_scripts.sc20211024overlord import start_script
from ultis.mouse_keyboard_automation import keyboard_type_job

userList = []
with open("C://Users//nxngu//Dropbox//AirdropProjects//user_db.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        userList.append(MyUser())
        userList[len(userList) - 1].init_by_row(row)

def checkMail(user):

    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()

    chromeCtrl.go_to_url('https://gmail.com/')

    time.sleep(5)

def changeTele(user):
    if user.id <=3:
        return
    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()

    pyautogui.click(205, 100)
    time.sleep(1)
    pyautogui.click(226, 717)
    time.sleep(1)
    pyautogui.click(1316, 615)
    time.sleep(1)
    pyautogui.click(1116, 459)
    pyautogui.click(1120, 551)
    # pyautogui.click(1120, 1055)


def twitterAddFr(theUser, userList):
    chromeCtrl = ChromeController(theUser)
    chromeCtrl.chrome_open()
    for user in userList:
        if user.id != theUser.id:
            chromeCtrl.tweeter_follow(user.twitterProfileLink)


# twitterAddFr(userList[0], userList)

for i in range(1, 11):
    userId = i
    user: MyUser = userList[userId - 1]
    checkMail(user)