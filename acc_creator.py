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

import pyautogui

from modules.captcha_warning import captcha_warning
from modules.chrome_jobs import ChromeController
from modules.user_model import MyUser
from ultis.mouse_keyboard_automation import keyboard_type_job

# import acc_creator_scripts.csv_reader

userList = []
with open("user_db.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        userList.append(MyUser())
        userList[len(userList) - 1].init_by_row(row)

# for myUser in userList:
#     if myUser.num == 1:
#         print(myUser.calculate_age())


def createDiscord(user):

    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()
    chromeCtrl.go_to_url('https://discord.com/register')

    # pyautogui.click(212, 671)


    pyautogui.click(1229, 578)
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



def createGmail(user):
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




#===========================================================
def initTelegramAccount(user):
    chromeCtrl = ChromeController(user)
    chromeCtrl.chrome_open()

    chromeCtrl.go_to_web_tele()

    print('User ' + str(user.phoneNumber) + ' ====================================')
    time.sleep(8)

    pyautogui.click(1448, 1322)
    time.sleep(2)

    pyautogui.click(1416, 1256)

    keyboard_type_job(user.phoneNumber[1:])


    pyautogui.click(1418, 1586)
    captcha_warning()

    pyautogui.click(221, 219)

    time.sleep(1)
    pyautogui.click(303, 305)

    time.sleep(1)

    pyautogui.click(1472, 1697)


    keyboard_type_job('https://t.me/joinchat/mAWmlIfVB59hOGY1')

    pyautogui.click(2334, 1738)
    time.sleep(1)

    pyautogui.click(1957, 1600)
    time.sleep(2)

    pyautogui.click(1688, 1033)
    time.sleep(1)
    #=============================================
    pyautogui.rightClick(237, 474)

    time.sleep(1)

    pyautogui.click(382, 777)

    time.sleep(1)
    #=============================================

    pyautogui.rightClick(237, 474)

    time.sleep(1)

    pyautogui.click(382, 777)

    time.sleep(1)

    chromeCtrl.chrome_close()


#===============================================

def createTelegramOnBlueStack(user):
    # pyautogui.click(1034, 777)
    # keyboard_type_job('84')
    # keyboard_type_job(user.phoneNumber)
    # pyautogui.press('enter')
    # captcha_warning()



    pyautogui.click(1240, 757)

    firstName = user.name.split(' ')[0]
    lastName = user.name.split(' ')[1]

    keyboard_type_job(firstName)
    time.sleep(1)

    pyautogui.press('tab')

    keyboard_type_job(lastName)
    pyautogui.press('enter')


    # pyautogui.click(1611, 1214)


theUser = userList[1]
pyautogui.click(197, 65)

captcha_warning()

# createTelegramOnBlueStack(theUser)
# initTelegramAccount(theUser)
# createGmail(theUser)
# createDiscord(theUser)