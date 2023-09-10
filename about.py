import curses
import _curses


def show_about_screen(stdscr: curses.window) -> None:
	while True:
		stdscr.clear()
		try:
			stdscr.addstr(
				1,
				0,
				"Hello, I'm Gourav Saini, and I've created 'ttyping' to improve typing skills in the terminal. Your contributions to 'ttyping' are most welcome!",
			)
		except _curses.error as e:
			pass
		key = stdscr.getch()
		if key == curses.KEY_ENTER or key in [10, 13]:
			break
