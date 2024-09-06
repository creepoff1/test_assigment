from BaseClass import BaseTest
from tests.PageObject.cart_page import CartPage
from tests.PageObject.main_page import MainPage
from tests.PageObject.product_page import ProductPage

class TestItemOrder(BaseTest):

    def test_catalog_tablets(self, driver, test_data):
        category = test_data["category"]
        subcategory = test_data["subcategory"]
        subsubcategory = test_data["subsubcategory"]
        destination = 'https://mega.readyscript.ru/catalog/digma/'
        product_name = "Планшет Digma iDx10 8Gb"

        main_page = MainPage(driver)
        main_page.click_product_link()
        main_page.select_category(category)
        main_page.select_sub_category(subcategory)
        main_page.click_sub_subcategory(subsubcategory, destination)

        product_page = ProductPage(driver)
        product = product_page.find_product_by_title(product_name).text
        assert product, "Product not found!"

    def test_add_and_clean_tablet_to_cart(self, driver, test_data):
        category = test_data["category"]
        subcategory = test_data["subcategory"]
        subsubcategory = test_data["subsubcategory"]
        destination = 'https://mega.readyscript.ru/catalog/digma/'
        product_name = "Планшет Digma iDx10 8Gb"

        main_page = MainPage(driver)
        main_page.click_product_link()
        main_page.select_category(category)
        main_page.select_sub_category(subcategory)
        main_page.click_sub_subcategory(subsubcategory, destination)

        product_page = ProductPage(driver)
        product = product_page.find_product_by_title(product_name).text
        assert product, "Product not found!"
        product_page.click_add_to_cart_button(product_name)
        product_page.click_cart_button()

        cart_page = CartPage(driver)
        cart_product = cart_page.find_item_in_cart_by_title(product_name)
        assert cart_product, "Product not found!"
        cart_page.clear_cart()
        main_page.click_cart_button()
        cart_page.empty_cart()
        assert "Корзина пуста", "Cart not empty!"
        cart_page.back_to_main()


