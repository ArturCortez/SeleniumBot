# SeleniumBot

### 1. Summary: This is an exercise as part of the recruitment process. The script must instantiate a Selenium Bot, make it access a given page and fill out a form, then extract some information from the page and store it in memory. That information will be used on a different process that calls pyautogui to write down the information on a Notepad and save it to the user's desktop.

### 2. Features: 
1. Access URL defined by .env
2. Fill out the form with the variables defined by .env
3. Set to Press the SEND button on the form or not
4. Use TypeWriter, to write using pyautogui
5. Choose Listwriter to save document using With Open instead of TypeWriter
6. If both typewriter and Listwriter are false, will write to Notepad using pyperclip


### 3. Tech Stack and Libraries:
+ Python, Selenium, Webdriver-Manager, Pyautogui, Pyperclip


### 4. Instalation:
+ Clone this repository, 
+ Create a virtual environment with python -m venv venv
+ Install dependencies with python -m pip install -r requirements.txt
+ open the .env-template in your notepad and fill out the necessary variables and options and save it as .env
+ run: python controller.py

