import pytest
from BaseClass import BaseTest
from tests.PageObject.cart_page import CartPage
from tests.PageObject.main_page import MainPage
from tests.PageObject.product_page import ProductPage


class TestItemOrder(BaseTest):

    def test_catalog_tablets(self, driver, test_data):
        category = test_data["category"]
        subcategory = test_data["subcategory"]
        subsubcategory = test_data["subsubcategory"]
        product_name = test_data["product_name"]

        main_page = MainPage(driver)
        main_page.click_product_link()
        main_page.select_and_click_subsubcategory(category, subcategory, subsubcategory)

        product_page = ProductPage(driver)
        product = product_page.find_product_by_title(product_name).text
        if not product:
            pytest.fail(f"Product '{product_name}' not found in category '{subsubcategory}'!")


    def test_add_and_clean_tablet_to_cart(self, driver, test_data):
        category = test_data["category"]
        subcategory = test_data["subcategory"]
        subsubcategory = test_data["subsubcategory"]
        product_name = test_data["product_name"]

        main_page = MainPage(driver)
        main_page.click_product_link()
        main_page.select_and_click_subsubcategory(category, subcategory, subsubcategory)
        product_page = ProductPage(driver)
        product = product_page.find_product_by_title(product_name).text
        if not product:
            pytest.fail(f"Product '{product_name}' not found in category '{subsubcategory}'!")
        product_page.click_add_to_cart_button(product_name)
        product_page.click_cart_button()

        cart_page = CartPage(driver)
        cart_product = cart_page.find_item_in_cart_by_title(product_name)
        if not cart_product:
            pytest.fail(f"Product '{product_name}' not found in the cart!")
        cart_page.clear_cart()
        main_page.click_cart_button()
        pytest.assume(cart_page.empty_cart(), "Cart is not empty after clearing!")
        cart_page.back_to_main()
