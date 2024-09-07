from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver


    def find_item_in_cart_by_title(self, product_name):
        try:
            item_text = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{product_name}')]"))
            )
            return item_text
        except Exception as e:
            return None


    def clear_cart(self):
        clear_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Очистить')]"))
        )
        clear_cart_button.click()


    def empty_cart(self):
        empty_cart_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Корзина пуста')]"))
        )
        return empty_cart_text.text


    def back_to_main(self):
        back_to_main_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Вернуться на главную')]"))
        )
        back_to_main_button.click()
