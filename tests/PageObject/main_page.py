from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver


    def click_icon_lk(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[@class='ms-2' and text()='Личный кабинет']"))
        ).click()


    def click_login_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Вход')]"))
        ).click()


    def click_logout_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-bs-toggle='dropdown']//*[name()='svg']"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Выход')]"))
        ).click()


    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='input-auth1']"))
        )
        email_input.clear()
        email_input.send_keys(email)


    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='input-auth2']"))
        )
        password_input.clear()
        password_input.send_keys(password)


    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Войти')]"))
        ).click()


    def get_logged_in_username(self, username):
        user_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//span[@class='ms-2' and text()='{username}']"))
        )
        return user_element.text


    def click_product_link(self):
        product_link = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".d-xl-block"))
        )
        product_link.click()


    def select_category(self, category_name):
        category = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='head-dropdown-catalog__categories py-xl-6 py-4']//a"))
        )
        for element in category:
            if element.text == category_name:
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                break


    def select_sub_category(self, subcategory_name):
        sub_category = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='head-dropdown-catalog__subcat-list']//a"))
        )
        for element in sub_category:
            if element.text == subcategory_name:
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                break


    def click_sub_subcategory(self, sub_subcategory_name):
        sub_subcategory = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@id='dropdown-subsubcat-2-2']//ul//li//a"))
        )
        for link in sub_subcategory:
            if link.text == sub_subcategory_name:
                link.click()
                break

    def select_and_click_subsubcategory(self, category_name, subcategory_name, subsubcategory_name):
        self.select_category(category_name)
        self.select_sub_category(subcategory_name)
        self.click_sub_subcategory(subsubcategory_name)

    def click_cart_button(self):
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "rs-cart"))
        )
        cart_button.click()


    def click_contacts_link(self):
        contacts_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'контакты')]"))
        )
        contacts_link.click()