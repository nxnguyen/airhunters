import pyperclip
from pynput.mouse import Button, Listener

print('AUTOSPY running')


def on_move(x, y):
    # print("Mouse moved to ({0}, {1})".format(x, y))
    pass


def on_click(x, y, button, pressed):
    if pressed:
        # print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        if button == Button.right:
            print('\n')
            # print('#========================================\n')
            print('pyautogui.click({0}, {1})\n'.format(x, y))
            pyperclip.copy('pyautogui.click({0}, {1})\n'.format(x, y))
    pass


def on_scroll(x, y, dx, dy):
    # print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    pass


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
