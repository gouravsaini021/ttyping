import curses
import _curses
import os
import time
import sys
import json


from cur_type import typing_screen
from lesson import show_lesson_screen
from setting import setting_screen

menu = ["Play", "Setting", "About", "Exit"]
menu_dict = {menu[i]: i for i in range(0, len(menu))}


def show_menu_scr(stdscr:curses.window, selected_row_idx:int) -> None:
    """This Function shows the menu/home screen."""
    stdscr.clear()
    try:
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
    except _curses.error as e:
        stdscr.addstr("Please resize your screen")
    stdscr.refresh()


def main(stdscr) -> None:
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
                typing_screen(stdscr, lesson_no)
            elif current_row_idx == menu_dict["Exit"]:
                curses.endwin()
                break
            elif current_row_idx == menu_dict["Setting"]:
                setting_screen(stdscr)
            elif current_row_idx == menu_dict["About"]:
                from about import show_about_screen
                show_about_screen(stdscr)

        show_menu_scr(stdscr, current_row_idx)
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
