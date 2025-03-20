import os, time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from file_writer import list_writer
from write_to_notepad import open_notepad_and_annotate

load_dotenv()
env_vars = os.environ

class ChromeBot:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def _wait_for_element(self, element_attr, attr_value, wait_time=10,):
        By_attr = getattr(By, element_attr)
        WebDriverWait(self.driver, timeout=wait_time).until(
            EC.presence_of_element_located((By_attr, attr_value))
        )

    def open_site(self, url):
        self.driver.get(url)

    def access_iframe(self, element_attr, attr_value):
        self._wait_for_element(element_attr, attr_value)
        By_attr = getattr(By, element_attr)
        iframe = self.driver.find_element(By_attr, attr_value)
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", iframe)
        
        time.sleep(0.5)
        
        self.driver.switch_to.frame(iframe)
        print("Switched to Frame")

    def access_default_dom(self):
        self.driver.switch_to.default_content()
        print("Switched back to main dom")

    def send_keys_by_id(self, element_id, answer):
        self._wait_for_element("ID", element_id)
        form_field = self.driver.find_element(By.ID, element_id)
        form_field.send_keys(answer)
        print(f"\nKeys Sent! {element_id} - {answer}")
        print()

    def click_by_id(self, element_id):
        self._wait_for_element(element_attr="ID", attr_value=element_id)
        button = self.driver.find_element(By.ID, element_id)
        button.click()
        print(f"\nElement Clicked! {element_id}")

    def click_by_attr(self, element_attr, attr_value):
        self._wait_for_element(element_attr, attr_value)
        By_attr = getattr(By, element_attr)
        element = self.driver.find_element(By_attr, attr_value)
        element.click()

    def get_text_by_attr(self, element_attr, attr_value):
        self._wait_for_element(element_attr, attr_value)
        By_attr = getattr(By, element_attr)
        element = self.driver.find_element(By_attr, attr_value)
        print(element.text)
        return element.text
    
    def get_texts_by_attr(self, element_attr, attr_value):
        self._wait_for_element(element_attr, attr_value)
        By_attr = getattr(By, element_attr)
        elements = self.driver.find_elements(By_attr, attr_value)
        text_list = []
        for element in elements:
            print(element.text)
            text_list.append(element.text)
        return text_list

    def close_browser(self):
        self.driver.quit()

    



