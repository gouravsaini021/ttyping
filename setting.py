import curses
import json
from app_configurations import get_address


def show_setting_screen(stdscr: curses.window, command: str = "audio") -> None:
	file_path = get_address("config")
	with open(file_path, "r") as file:
		config_file = json.load(file)
	Audio = config_file["audio"]
	stdscr.clear()
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	y, x = stdscr.getmaxyx()
	y, x = y // 2, x // 2
	stdscr.addstr(y, x, "Audio: " + str(Audio))
	stdscr.addstr(y + 1, x + 2, "Home")
	if command == "audio":
		stdscr.addstr(y, x + 7, str(Audio), curses.color_pair(1))
	else:
		stdscr.addstr(y + 1, x + 2, "Home", curses.color_pair(1))
	stdscr.refresh()


def change_audio_setting() -> None:
	file_path = get_address("config")
	with open(file_path, "r") as file:
		config = json.load(file)

	if config["audio"]:
		config["audio"] = 0
	else:
		config["audio"] = 1

	with open(file_path, "w") as file:
		json.dump(config, file, indent=4)


def setting_screen(stdscr: curses.window) -> None:
	current_cursor_point = "audio"
	show_setting_screen(stdscr)
	while True:
		key = stdscr.getch()
		if key == curses.KEY_UP or key == curses.KEY_DOWN:
			if current_cursor_point == "audio":
				current_cursor_point = "home"
			else:
				current_cursor_point = "audio"
			show_setting_screen(stdscr, current_cursor_point)

		elif key == curses.KEY_ENTER or key in [10, 13]:
			if current_cursor_point == "audio":
				change_audio_setting()
				show_setting_screen(stdscr, current_cursor_point)
			else:
				break
