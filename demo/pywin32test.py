import os.path
import time
import os,shutil

from pykeyboard import PyKeyboard
from pymouse import PyMouse

if __name__ == '__main__':
    path = "D:\FFOutput\屏幕录像"
    file_list = os.listdir(path)

    for i in file_list:
        if os.path.isfile(os.path.join(path,i)):
            file_path = os.path.join(path,i)
            print(file_path)
            shutil.move(file_path,"D:\\FFOutput\\屏幕录像\\2022_01_18 16_45_44屏幕录像\\3.txt")




