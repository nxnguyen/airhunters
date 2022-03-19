import csv
import time
from datetime import datetime

import pyautogui
import pyperclip
from faker import Faker

from modules.captcha_warning import captcha_warning
from modules.chrome_jobs import ChromeController
from modules.user_model import MyUser
from ultis.mouse_keyboard_automation import keyboard_type_job

# import acc_creator_scripts.csv_reader

userList = []
with open("C://Users//nxngu//Dropbox//AirdropProjects//user_db.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        userList.append(MyUser())
        userList[len(userList) - 1].init_by_row(row)

def getDiscordID(user):
    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    chromeCtrl.go_to_discord()
    time.sleep(2)

    pyautogui.click(457, 1765)
    user.discordId = pyperclip.paste()
    chromeCtrl.chrome_close()


def getTwitterID(user):
    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    chromeCtrl.go_to_twitter()

    pyautogui.click(429, 1734)

    time.sleep(1)
    pyautogui.doubleClick(458, 1375)

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    user.twitterId = pyperclip.paste()
    chromeCtrl.chrome_close()


for i in range(2):
    theUser = userList[i]

    pyautogui.click(216, 145)

    getTwitterID(theUser)
    time.sleep(1)
    getDiscordID(theUser)

#==============================================================

faker = Faker()
rows = []
with open("C://Users//nxngu//Dropbox//AirdropProjects//user_db.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    # print(header)
    for row in csvreader:
        rows.append(row)
        row[2] = userList[int(row[0]) - 1].discordId
        row[3] = userList[int(row[0]) - 1].twitterId


filename = 'C://Users//nxngu//Dropbox//AirdropProjects//user_db_updated.csv'
with open(filename, 'w') as file:
    for header in header:
        file.write(str(header) + ',')
    file.write('\n')
    for row in rows:
        # print(row)
        for x in row:
            file.write(x + ',')
        file.write('\n')

with open("C://Users//nxngu//Dropbox//AirdropProjects//user_db_updated.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    # print(header)
    for row in csvreader:
        rows.append(row)
        # print(row)
