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
from modules.user_model import MyUser
from airdrop_scripts.sc20211020helloworld import start_script

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


start_script(userList)