import pyautogui
import pyperclip
from pynput.keyboard import Key, Controller

from modules.captcha_warning import captcha_plus_solver
from ultis.mouse_keyboard_automation import keyboard_type_job
import subprocess
import time
from pywinauto import application
from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError
from subprocess import Popen, PIPE


class TelegramController:

    def __init__(self, user):
        self.user = user
        self.app = application.Application()
        pass

    def telegram_open(self):
        string_id = f"{self.user.id:03}"
        stringRun = 'C:\Airhunters\Telegram' + string_id + '\Telegram.exe --start-maximized'
        # print(stringRun)
        subprocess.Popen(
            r'' + stringRun,
            stderr=subprocess.PIPE)
        time.sleep(3)
        pyautogui.click(2160, 286)

    def telegram_close(self):
        pyautogui.click(2689, 24)
        pass

    def telegram_join_channel(self, url):
        time.sleep(1)
        pyautogui.click(199, 85)
        time.sleep(1)
        pyautogui.click(622, 110)

        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite(["backspace"])
        keyboard_type_job(url)
        time.sleep(3)
        pyautogui.click(2100, 1686)
        pyautogui.typewrite(["enter"])
        time.sleep(1)
        pyautogui.click(1852, 1664)
        time.sleep(1)
        pyautogui.click(1623, 1779)
        time.sleep(2)
        pass

    def telegram_note_down(self, note):
        time.sleep(1)
        pyautogui.click(199, 85)
        time.sleep(1)
        pyautogui.click(622, 110)

        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite(["backspace"])
        keyboard_type_job(note)
        time.sleep(3)
        pyautogui.click(2100, 1686)
        pyautogui.typewrite(["enter"])
        time.sleep(1)
        pass

    def telegram_press_level(self, level):
        if level == 1:
            pyautogui.click(1608, 1765)
        if level == 2:
            pyautogui.click(1594, 1675)
        if level == 3:
            pyautogui.click(1606, 1582)
        if level == 4:
            pyautogui.click(1567, 1478)

    def telegram_solve_number_equal_captcha(self):
        time.sleep(1)
        pyautogui.rightClick(1494, 1554)
        time.sleep(0.5)
        pyautogui.click(1565, 1240)

        time.sleep(0.5)
        pyautogui.click(1549, 1669)

        time.sleep(3)

        answer = captcha_plus_solver(pyperclip.paste())
        return answer
