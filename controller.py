import os, time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from chrome_bot import ChromeBot
from file_writer import list_writer
from write_to_notepad import open_notepad_and_annotate, open_notepad_and_paste_from_memory

load_dotenv()
env_vars = os.environ


def main():
    '''
    
    Fale Conosco: //*[@id="menu-item-1249"]/a
    name: //*[@id="firstname-cad1a681-b00d-4619-8daf-7496d8bbb5db"]
    email: //*[@id="email-cad1a681-b00d-4619-8daf-7496d8bbb5db"]
    phone: //*[@id="phone-cad1a681-b00d-4619-8daf-7496d8bbb5db"]
    realter: //*[@id="sou_corretor0-cad1a681-b00d-4619-8daf-7496d8bbb5db"]
    message: //*[@id="message-cad1a681-b00d-4619-8daf-7496d8bbb5db"]
    consent: //*[@id="LEGAL_CONSENT.subscription_type_252646919-cad1a681-b00d-4619-8daf-7496d8bbb5db"]
    envar: //*[@id="hsForm_cad1a681-b00d-4619-8daf-7496d8bbb5db"]/div[7]/div[2]/input

    '''
    elements = {
        "iframe": {"attribute": "ID", "value": "hs-form-iframe-0"},
        "Fale Conosco": {"attribute": "CLASS_NAME", "value": "title"},
        "name": "firstname-cad1a681-b00d-4619-8daf-7496d8bbb5db",
        "email": "email-cad1a681-b00d-4619-8daf-7496d8bbb5db",
        "phone": "phone-cad1a681-b00d-4619-8daf-7496d8bbb5db",
        "realter": {"attribute": "NAME", "value": "sou_corretor"},
        "message": "message-cad1a681-b00d-4619-8daf-7496d8bbb5db",
        "consent": "LEGAL_CONSENT.subscription_type_252646919-cad1a681-b00d-4619-8daf-7496d8bbb5db",
        "send_button": {"attribute": "XPATH", "value": "//*[@id='hsForm_cad1a681-b00d-4619-8daf-7496d8bbb5db']/div[7]/div[2]/input"}
    }

    bot = ChromeBot()
    bot.open_site(url=env_vars["FALE_CONOSCO_URL"])

    if not bot.driver.current_url == env_vars["FALE_CONOSCO_URL"]:
        bot.click_by_attr(elements["Fale Conosco"]["attribute"], elements["Fale Conosco"]["value"])
    
    time.sleep(2)
    bot.access_iframe(elements["iframe"]["attribute"], elements["iframe"]["value"])
    
    bot.click_by_attr(elements["realter"]["attribute"], elements["realter"]["value"])
    bot.click_by_id(elements.get("consent"))


    bot.send_keys_by_id(elements.get("name"), str(env_vars["NAME"]))
    bot.send_keys_by_id(elements.get("email"), str(env_vars["EMAIL"]))
    bot.send_keys_by_id(elements.get("phone"), str(env_vars["PHONE"]))
    bot.send_keys_by_id(elements.get("message"), str(env_vars["MESSAGE"]))
    
    bot.access_default_dom()
    time.sleep(0.5)

    if env_vars["PRESS_SEND"].lower() == "true":
        bot.click_by_id(elements["send_button"]["attribute"], elements["send_button"]["value"])

    text_list = bot.get_texts_by_attr("CLASS_NAME", "icon-box-description")
    time.sleep(0.5)
    bot.close_browser()

    if env_vars["USE_TYPEWRITER"].lower() == "true":
        print("Writing to Notepad")
        open_notepad_and_annotate(text_list)
    elif env_vars["USE_LISTWRITER"].lower() == "true":
        list_writer("prova_gc.txt", text_list)
    else:
        print("Writing to Notepad")
        open_notepad_and_paste_from_memory(text_list)

    



if __name__ == "__main__":
    main()