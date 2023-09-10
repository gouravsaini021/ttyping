import os
import shutil
import sys


def get_endpoint_address(file_name: str) -> str:
	all_addresses = {
		"config": "config.json",
		"lesson": "lesson.json",
		"typewriter_sound": os.path.join("audio", "typewriter.mp3"),
		"error_sound": os.path.join("audio", "error.mp3"),
	}
	return all_addresses[file_name]


def get_address(file_name: str) -> str:
	import logging

	endpoint_address = get_endpoint_address(file_name)
	# Check if the script is run as a standalone executable (PyInstaller)
	if getattr(sys, "frozen", False):
		home_dir = os.path.expanduser("~")
		file_path = os.path.join(home_dir, ".config", "ttyping", endpoint_address)

		# chceck if path exists
		if os.path.isfile(file_path):
			return file_path
		else:
			# The path doesn't exists so it copy all file in .config/ttyping
			copy_all_file_config_folder()
			return file_path
	else:
		# The script is executed directly using the Python interpreter
		return get_endpoint_address(file_name)


def copy_all_file_config_folder():
	# Get the user's home directory
	home_dir = os.path.expanduser("~")

	# Construct the destination path in the .config directory
	config_dir = os.path.join(home_dir, ".config", "ttyping")

	# Create the .config directory if it doesn't exist
	if not os.path.exists(config_dir):
		os.makedirs(os.path.join(config_dir, "audio"))

	for file_name in ["config", "lesson", "typewriter_sound", "error_sound"]:
		destination_file = os.path.join(config_dir, get_endpoint_address(file_name))
		source_file = os.path.join(sys._MEIPASS, get_endpoint_address(file_name))
		
		# copy file from pyinstaller executable to user .config/ttyping
		shutil.copy(source_file, destination_file)
