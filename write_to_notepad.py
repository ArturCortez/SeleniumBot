import os
import pyautogui
import time
import subprocess
import pyperclip
from dotenv import load_dotenv

load_dotenv()
env_vars = os.environ

def open_notepad_and_annotate(annotation):
    try:
        subprocess.Popen("notepad.exe")
        time.sleep(1)

        for text in annotation:
            pyautogui.typewrite(text, interval=0.05)
            pyautogui.press('enter')
            time.sleep(0.2)

        string_path = env_vars["DESKTOP_PATH"]
        desktop_path = os.path.expanduser(string_path)

        pyautogui.hotkey('ctrl', 'shift', 's')
        pyautogui.typewrite(desktop_path, interval=0.05)
        pyautogui.press('enter')

    except Exception as e:
        print(f"Error Writing to Notepad: {e}")


def open_notepad_and_paste_from_memory(annotation):
    try:
        subprocess.Popen("notepad.exe")
        time.sleep(1)

        full_text = '\n'.join(annotation)
        pyperclip.copy(full_text)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1.2)
        
        string_path = env_vars["DESKTOP_PATH"]
        desktop_path = os.path.expanduser(string_path)

        pyautogui.hotkey('ctrl', 'shift', 's')
        pyautogui.typewrite(desktop_path, interval=0.05)
        pyautogui.press('enter')

    except Exception as e:
        print(f"Error Writing to Notepad: {e}")
