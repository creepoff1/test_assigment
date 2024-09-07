from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ContactsPage:

    def __init__(self, driver):
        self.driver = driver


    def check_presence_of_title_on_page(self, title):
        title_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//h1[contains(text(),'{title}')]"))
        )
        return title_element.text


    def click_to_back_to_main(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'главная')]"))
        ).click()
