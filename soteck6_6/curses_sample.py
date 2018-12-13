import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,'こんにちは')
    stdscr.addstr(1,10,'python curses')
    stdscr.addstr(2,0,'何かキーを押すと終了します。')
    stdscr.getkey()
    stdscr.refresh()

if __name__ == '__main__':
    curses.wrapper(main)
