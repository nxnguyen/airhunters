import pyautogui
import pyperclip
from pynput.keyboard import Key, Controller
from ultis.mouse_keyboard_automation import keyboard_type_job
import subprocess
import time
from pywinauto import application
from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError
from subprocess import Popen, PIPE


class ChromeController:

    def __init__(self, user):
        self.user = user
        self.app = application.Application()
        pass

    def chrome_open(self):
        stringRun = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --profile-directory="Profile ' + str(
            self.user.chromeProfileId) + '" --start-maximized'
        subprocess.Popen(
            r'' + stringRun,
            stderr=subprocess.PIPE)
        time.sleep(3)

    def chrome_close(self):
        pyautogui.click(2689, 24)
        pass

    def discord_join_invite(self, url):
        self.go_to_url(url)
        pyautogui.click(1439, 1204)
        time.sleep(3)
        pyautogui.click(1439, 1204)
        time.sleep(1)
        pass


    def tweeter_follow(self, url):
        self.go_to_url(url)
        pyautogui.click(1785, 699)
        time.sleep(1)
        pass

    def tweeter_quote_tweet(self, url, findQuoteBtnFunc, quoteFunc):
        self.go_to_url(url)
        findQuoteBtnFunc()

        # click retweet_btn
        x, y = pyautogui.locateCenterOnScreen('img_twitter\\retweet_btn.png', region=(1035, 0, 200, 1823),
                                              confidence=0.8)
        pyautogui.click(x, y)
        time.sleep(2)
        # click quote tweet
        x, y = pyautogui.locateCenterOnScreen('img_twitter\\quote_tweet_btn.png', region=(871, 0, 300, 1823),
                                              confidence=0.8)
        pyautogui.click(x, y)
        time.sleep(2)

        pyautogui.click(1166, 405)
        quoteFunc()
        time.sleep(2)
        pyautogui.scroll(-1000)
        time.sleep(2)
        x, y = pyautogui.locateCenterOnScreen('img_twitter\\tweet_send_btn.png', region=(1800, 0, 200, 1823),
                                              confidence=0.8, grayscale=True)
        pyautogui.click(x, y)

        time.sleep(2)
        pyautogui.click(1579, 1721)

        time.sleep(2)
        return self.copy_url_address()

    def copy_url_address(self):
        pyautogui.click(702, 105)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        return pyperclip.paste()

    def go_to_web_tele(self):
        self.go_to_url('https://web.telegram.org')
        pass

    def go_to_twitter(self):
        self.go_to_url('https://twitter.com/home?lang=en')
        pass

    def go_to_url(self, url):
        pyautogui.click(702, 105)

        time.sleep(1)
        keyboard_type_job(url)
        pyautogui.typewrite(["enter"])
        time.sleep(3)
        pass

    def tele_join_channel(self, url):
        # click Vao Saved Message
        time.sleep(1)
        pyautogui.click(221, 219)
        time.sleep(1)
        pyautogui.click(303, 305)
        time.sleep(1)
        pyautogui.click(1018, 1729)
        time.sleep(1)
        keyboard_type_job(url)
        time.sleep(3)
        # tat thong tin trang web
        pyautogui.click(879, 1634)
        time.sleep(1)
        pyautogui.typewrite(["enter"])
        time.sleep(1)
        # click vao link
        pyautogui.click(1815, 1612)
        time.sleep(1)
        # click join
        pyautogui.click(1738, 199)
        time.sleep(1)
        pass
