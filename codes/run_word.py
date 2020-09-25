import os
import time

def main():
    """
    屏幕上显示跑马灯文字
    """
    content = "你好！欢迎来到王者荣耀。。。。。"
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:]+content[0]

if __name__ == "__main__":
    main()
