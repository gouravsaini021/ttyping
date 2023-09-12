# About ttyping
- ttyping is a terminal-based typing practice tool written in Python, utilizing the curses module. 
- It offers a range of typing sessions suitable for users at various skill levels, spanning from beginner to advanced.
- Each lesson within the tool comes with a specific goal measured in words per minute (WPM).

# Some Snapshots:
 **Home screen**
 
![image](https://github.com/gouravsaini021/curses-typing/assets/63018500/81557e42-03aa-442e-81a1-1900158d04f4)

**Lesson screen**

![image](https://github.com/gouravsaini021/curses-typing/assets/63018500/f1141396-79cc-4873-995f-0c4f4c862385)

**Practice Screen**

![image](https://github.com/gouravsaini021/curses-typing/assets/63018500/7f47a07a-c994-4f93-914f-a53d2bf9bba3)

**Result Screen**

![image](https://github.com/gouravsaini021/curses-typing/assets/63018500/504e7891-b5c7-4ef7-9b17-2ec221dc4d5c)








# How to Run This Project

These instructions will guide you through the process of running this project on your system. Follow these steps carefully to ensure a successful execution.

## Via Cloning

### Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- [Python3](https://www.python.org/downloads/) (version 3.10 or higher)
- [Virtual Environment (venv)](https://docs.python.org/3/library/venv.html)

### Installation

1. **Clone the Project Repository:**

   Clone this project repository to your local machine using Git. Open your terminal or command prompt and navigate to the directory where you want to store the project:

   ```shell
   git clone https://github.com/gouravsaini021/ttyping
2. **Create and Activate a Virtual Environment:**
     ```shell
     cd ttyping
    python -m venv venv
     ```
     Activate the virtual environment:
        on windows:
        ```
          .\venv\Scripts\activate
          ```
        on linux or macOS:
       ```source venv/bin/activate```
4. **Install Project Dependencies:**
     ```shell
   pip install -r requirements.txt 
6. **Run the Python Script:**
   ```shell
   python3 main.py
   ```

## Using Docker 
  ### Prerequisites:
  
  Before you begin, make sure you have the Docker installed on your system:
  
  ### Installation:
   **Run the following command:**
      ```
      docker run -it gouravsaini/ttyping:2.0
      ```

  ## Download Pyinstaller Executables 

1. **Navigate to the Executable Folder:**

   Open your project directory, and you will see a folder named `Executable`.
2. **Choose Your Operating System Folder:**

   Inside the `Executable` folder, you will find subfolders named after various operating systems, such as Windows, macOS, or Linux. Select the folder that corresponds to your operating system.

3. **Locate the Executable:**

   Within your chosen operating system folder, you will find an executable file named `ttyping` and download it to your system.
4. **Run the Executable:**
   Go to the folder where the executable is downloaded via Terminal and run ```./ttyping ```
    
