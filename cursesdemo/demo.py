from unicurses import *

def main():
    myscr = initscr()
    # clear()
    # noecho()
    for i in range(0, 11):
        v = i-10
        addstr('aaaaa')
    # endwin()

    # 这里要通过获取输入卡住，不然直接就退出去了。
    getch()

main()