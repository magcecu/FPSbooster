# Prodused by The Mag Market # 
     # Made By MagCecu #

import psutil
from pystyle import Center
from colorama import init, Fore as cc
import winreg as reg
import os
import tempfile
import time
import ctypes
import sys
import win32api
import win32con


init()
r = R = cc.RED
print(f'{r}')

def clear_temp_folders():
    print("CLEARING ALL OF THE TEMPORARY FOLDERS/FILES")
    temp_dir = tempfile.gettempdir()

    total_size_bytes = 0

    try:
        # scan the files
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # get the size of the file and delete it
                    file_size = os.path.getsize(file_path)
                    total_size_bytes += file_size
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

        # size-gigs
        total_size_gb = total_size_bytes / (1024 ** 3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Temporary folders cleared. Total size cleared: {total_size_gb:.2f} GB")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Error clearing temporary folders: {e}")
    time.sleep(3)
    
def run_as_admin():
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if not is_admin:
            # If not, request admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit()
        else:
            print("Script is running with admin rights.")

    except Exception as e:
        print(f"An error occurred: {e}")

def disable_startup_apps_temporarily():
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        # Open the registry key with write access
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, key_path, 0, win32con.KEY_SET_VALUE)

        # Enumerate the values and delete each one
        i = 0
        while True:
            name, _, _ = win32api.RegEnumValue(key, i)
            win32api.RegDeleteValue(key, name)
            i += 1

        win32api.RegCloseKey(key)

    except FileNotFoundError:
        print("No startup apps found.")

    except Exception as e:
        print(f"An error occurred: {e}")


def restart_windows():
    os.system("shutdown /r /t 1")

logo = Center.XCenter("""
 ________       __  ___          __  ___         __       __ 
/_  __/ /  ___ /  |/  /__ ____ _/  |/  /__ _____/ /_____ / /_
 / / / _ \/ -_) /|_/ / _ `/ _ `/ /|_/ / _ `/ __/  '_/ -_) __/
/_/ /_//_/\__/_/  /_/\_,_/\_, /_/  /_/\_,_/_/ /_/\_\\__/\__/ 
                         /___/                              
                   Memory & Ram Opmitiser
              Imagine Downloading Free Ram lol                """)


info = Center.XCenter("""
This program will request a restart for clearing you cached ram!
                      
                      Pending processes:
                       -removing temps
          -clearing startup for the current session
             -restarting and clearing cached ram
""")

if __name__ == "__main__":
        
        #1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print()
        print(info)
        print()
        input(" Press enter to continue with the operation...")
        run_as_admin()

        #2
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print()
        print(info)
        print()
        print(Center.XCenter("...Clearing Temp folders..."))
        print()
        clear_temp_folders()
        
        #3
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print()
        print(Center.XCenter("...Restarting..."))
        time.sleep(2)

        disable_startup_apps_temporarily()
        restart_windows()
