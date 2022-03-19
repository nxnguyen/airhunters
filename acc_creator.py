# tao model #pass Uyen@1957@
# script follow fb
# script follow tweet va retweet
# script follow channel telegram
# script vuot captcha
# script follow discord
# tao medium linkedin


# python main.py
# python autospy.py

# import modules.csv_reader

import csv
import time
from datetime import datetime

import pyautogui

from modules.captcha_warning import captcha_warning
from modules.chrome_jobs import ChromeController
from modules.telegram_jobs import TelegramController
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

# for myUser in userList:
#     if myUser.num == 1:
#         print(myUser.calculate_age())


def createDiscordAcc(user):

    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    chromeCtrl.go_to_url('https://discord.com/register')

    # pyautogui.click(212, 671)


    time.sleep(1)
    keyboard_type_job(user.mail)
    pyautogui.press('tab')
    keyboard_type_job(user.mail.split('@gmail.com')[0])

    pyautogui.press('tab')
    keyboard_type_job(user.mailPass)

    pyautogui.press('tab')
    keyboard_type_job(str(user.birthDate.month))
    pyautogui.press('tab')
    keyboard_type_job(str(user.birthDate.day))
    pyautogui.press('tab')
    keyboard_type_job(str(user.birthDate.year))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')



def createGmailAcc(user):
    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    chromeCtrl.go_to_url('https://www.google.com/intl/en/gmail/about/#')

    pyautogui.click(2338, 202)
    time.sleep(2)



    firstName = user.name.split(' ')[0]
    lastName = user.name.split(' ')[1]

    pyautogui.click(924, 790)
    keyboard_type_job(firstName)
    time.sleep(1)

    pyautogui.click(1258, 798)

    keyboard_type_job(lastName)

    pyautogui.click(1082, 936)


    keyboard_type_job(user.mail.split('@gmail.com')[0])


    pyautogui.click(939, 1080)

    keyboard_type_job(user.mailPass)


    pyautogui.click(1215, 1076)
    keyboard_type_job(user.mailPass)

    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(1018, 998)

    keyboard_type_job(user.phoneNumber)


    captcha_warning()
    pyautogui.click(833, 1095)

    keyboard_type_job(user.birthDate.day)
    pyautogui.press('tab')
    # keyboard_type_job(user.birthDate.month)
    month = user.birthDate.month
    for i in range(month):
        pyautogui.press('down')

    pyautogui.press('tab')
    keyboard_type_job(user.birthDate.year)

    pyautogui.press('tab')
    pyautogui.press('down')



#===============================================
def logoutTelegramOnBlueStack():
    pyautogui.click(203, 364)
    time.sleep(1)
    pyautogui.click(372, 1102)
    time.sleep(1)
    pyautogui.click(1837, 515)
    time.sleep(1)
    pyautogui.click(1670, 713)
    time.sleep(1)
    pyautogui.click(1077, 1378)
    time.sleep(1)
    pyautogui.click(1799, 1158)
    time.sleep(1)
    pyautogui.click(1414, 1340)


#===============================================

def createTelegramOnBlueStack(user):
    pyautogui.click(1034, 777)
    keyboard_type_job('84')
    keyboard_type_job(user.phoneNumber)
    pyautogui.press('enter')
    captcha_warning()



    pyautogui.click(1240, 757)

    firstName = user.name.split(' ')[0]
    lastName = user.name.split(' ')[1]

    keyboard_type_job(firstName)
    time.sleep(1)

    pyautogui.press('tab')

    keyboard_type_job(lastName)
    pyautogui.press('enter')


    # pyautogui.click(1611, 1214)


def createTwitterAcc(user):
    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()

    chromeCtrl.go_to_url('https://twitter.com')

    captcha_warning()

    pyautogui.click(1836, 1053)
    time.sleep(3)
    pyautogui.click(1507, 862)
    time.sleep(1)

    pyautogui.click(1723, 1132)

    time.sleep(2)


    month = user.birthDate.month
    for i in range(month):
        pyautogui.press('down')
    pyautogui.press('tab')
    day = user.birthDate.day
    for i in range(day):
        pyautogui.press('down')
    pyautogui.press('tab')
    for i in range(datetime.now().year + 1 - user.birthDate.year):
        pyautogui.press('down')

    time.sleep(2)
    pyautogui.click(1501, 1519)
    time.sleep(1)
    pyautogui.click(1501, 1519)
    time.sleep(3)
    pyautogui.click(1501, 1519)

    time.sleep(2)

    pyautogui.click(1400, 1279)

    time.sleep(1)

    pyautogui.click(1427, 984)
    time.sleep(1)
    pyautogui.click(1903, 1491)

    time.sleep(1)

    pyautogui.click(1501, 1519)
    time.sleep(1)

    pyautogui.click(1501, 1519)

def openGmail(user):
    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    chromeCtrl.go_to_gmail()

def createFbAcc(user):

    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    chromeCtrl.go_to_fb()

    pyautogui.click(2004, 1000)
    time.sleep(1)

    firstName = user.name.split(' ')[0]
    lastName = user.name.split(' ')[1]

    keyboard_type_job(firstName)
    time.sleep(1)

    pyautogui.press('tab')

    keyboard_type_job(lastName)
    pyautogui.press('tab')

    keyboard_type_job(user.mail)
    pyautogui.press('tab')
    keyboard_type_job(user.mail)
    pyautogui.press('tab')
    keyboard_type_job(user.mailPass)
    pyautogui.press('tab')
    pyautogui.press('tab')
    keyboard_type_job(user.birthDate.day)

    pyautogui.press('tab')

    for i in range(12):
        pyautogui.press('up')

    month = user.birthDate.month
    for i in range(month - 1):
        pyautogui.press('down')

    pyautogui.press('tab')
    for i in range(datetime.now().year - user.birthDate.year):
        pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.press('tab')

    pyautogui.press('down')
    pyautogui.press('up')





def initTelegram(user):
    teleCtrl = TelegramController(user)
    teleCtrl.telegram_open()

    pyautogui.click(1442, 1123)
    time.sleep(1)
    pyautogui.click(1430, 1267)
    time.sleep(1)
    pyautogui.typewrite(["backspace"])
    pyautogui.typewrite(["backspace"])

    keyboard_type_job(84)
    keyboard_type_job(user.phoneNumber)
    pyautogui.typewrite(["enter"])
    captcha_warning()

    pyautogui.click(203, 97)
    time.sleep(1)
    pyautogui.click(627, 112)
    time.sleep(1)

    keyboard_type_job('https://t.me/joinchat/mAWmlIfVB59hOGY1')
    pyautogui.typewrite(["enter"])
    time.sleep(1)
    pyautogui.click(1639, 1676)
    time.sleep(1)
    pyautogui.click(1671, 1187)

    time.sleep(1)

    pyautogui.rightClick(646, 337)
    time.sleep(1)
    pyautogui.click(543, 412)
    time.sleep(1)
    pyautogui.rightClick(522, 337)
    time.sleep(1)
    pyautogui.click(681, 437)
    time.sleep(1)

    time.sleep(1)

    pyautogui.click(194, 98)
    time.sleep(1)
    pyautogui.click(359, 635)
    time.sleep(1)
    pyautogui.click(1300, 519)
    time.sleep(1)
    pyautogui.click(1329, 895)
    time.sleep(1)

    keyboard_type_job(user.teleUsername)
    pyautogui.typewrite(["enter"])


theUser = MyUser()
theUser = userList[9]
pyautogui.click(216, 145)

# logoutTelegramOnBlueStack()
# createTelegramOnBlueStack(theUser)
# initTelegram(theUser)
# createGmailAcc(theUser)
# createDiscordAcc(theUser)
# openGmail(theUser)
# createTwitterAcc(theUser)
# createFbAcc(theUser)



