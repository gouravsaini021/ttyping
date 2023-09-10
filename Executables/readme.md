# Creating an Executable for Your Project with PyInstaller

These instructions guide you through the process of creating an executable PyInstaller. Please follow these steps carefully.

## Prerequisites

Before proceeding, ensure you have PyInstaller installed on your system.

## Steps

1. **Navigate to Your Project Directory:**

   Open your terminal or command prompt and change your current working directory to the location of your project's files using the `cd` command:

   ```shell
   cd ttpying
   ```
2. **Run the following command:**

    ```shell
    pyinstaller --add-data "config.json:." --add-data "lesson.json:." --add-data "audio/error.mp3:./audio" --add-data "audio/typewriter.mp3:./audio" --onefile main.py --name ttyping
    ```
    note : if you are using windows then change : to ; in above command

3. **Location of exectuable file:**
    you can find you executable in dist folder
