import curses
import logging
import time
from cur_type import get_xxxxx
from lesson import show_lesson_screen

menu = ["Home", "Play", "Setting", "Exit"]
menu_dict = {menu[i]: i for i in range(0, len(menu))}

logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="%(asctime)s, %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


def show_menu_scr(stdscr, selected_row_idx):
    """This Function shows the menu/home screen."""
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for index, row in enumerate(menu):
        y = h // 2 - len(menu) + index
        x = w // 2 - len(menu)
        if index == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row_idx = 0
    show_menu_scr(stdscr, current_row_idx)
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP:
            if current_row_idx == 0:
                current_row_idx = len(menu) - 1
            else:
                current_row_idx -= 1
        elif key == curses.KEY_DOWN:
            if current_row_idx == len(menu) - 1:
                current_row_idx = 0
            else:
                current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row_idx == menu_dict["Play"]:
                lesson_no = show_lesson_screen(stdscr)
                get_xxxxx(stdscr, lesson_no)
            elif current_row_idx == menu_dict["Exit"]:
                curses.endwin()
                break
            elif current_row_idx == menu_dict["Setting"]:
                pass
                # setting_screen(stdscr)

        show_menu_scr(stdscr, current_row_idx)
        stdscr.refresh()

        #     stdscr.clear()
    #     stdscr.addstr(0, 0, str(key))
    #     stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
