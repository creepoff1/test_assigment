from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def find_product_by_title(self, product_name):
        # Найти все карточки товаров
        product_cards = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='item-card__inner']"))
        )
        for card in product_cards:
            try:
                product_title = card.find_element(By.XPATH, ".//a[@class='item-card__title rs-to-product']")
                if product_name in product_title.text:
                    return card
            except:
                continue
        return None

    def click_add_to_cart_button(self, product_name):
        product_card = self.find_product_by_title(product_name)

        if product_card:
            try:
                add_to_cart_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, ".//span[text()='В корзину']"))
                )
                actions = ActionChains(self.driver)
                actions.move_to_element(add_to_cart_button).click().perform()
            except Exception as e:
                print(f"Failed to find or click 'В корзину' button: {e}")

    def click_cart_button(self):
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='btn btn-primary w-100']"))
        )
        cart_button.click()
