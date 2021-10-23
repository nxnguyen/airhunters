import random
import subprocess
import sys
import time
from pywinauto import application
from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError
from subprocess import Popen, PIPE


def bring_telegram_to_front():
    # bring_window_to_front('Telegram Desktop (32 bit)')
    bring_window_to_front(r"C:\Users\nxngu\AppData\Roaming\Telegram Desktop\Telegram.exe", 'Telegram')


def bring_window_to_front(path, class_name):
    app = application.Application()
    try:
        print('Select class window "%s"' % class_name)
        app.connect(path=path, class_name=class_name)
        # app.connect(title_re=".*%s.*" % class_name)
        # app.connect(title_re=class_name)

        # Access app's window object
        app_dialog = app.top_window()

        # app_dialog.minimize()
        # app_dialog.restore()
        app_dialog.maximize()
        app_dialog.set_focus()

    except WindowNotFoundError:
        print('WindowNotFoundError')

        print
        '"%s" not found' % class_name

        pass
    except WindowAmbiguousError:
        print
        'There are too many "%s" windows found' % class_name
        pass
    except:
        print('EXCEPTION -> RUNNING EXE')
        subprocess.Popen(r"C:\Users\nxngu\AppData\Roaming\Telegram Desktop\Telegram.exe", stderr=subprocess.PIPE)

        time.sleep(5)
        bring_window_to_front(path, class_name)
        pass
