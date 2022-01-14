import time

from pykeyboard import PyKeyboard
from pymouse import PyMouse

if __name__ == '__main__':
    # k = PyKeyboard()
    # k.press_key(k.function_keys[6])
    # time.sleep(3)
    # k.press_key(k.function_keys[8])

    mouse = PyMouse()

    x_dim, y_dim = mouse.screen_size()  # 获得屏幕尺寸
    print(x_dim,y_dim)
    mouse.move(1000,900)




