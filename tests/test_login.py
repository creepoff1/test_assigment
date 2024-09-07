import pytest

from BaseClass import BaseTest
from tests.PageObject.main_page import MainPage

class TestLogin(BaseTest):

    def test_successful_login(self, driver, test_data):
        main_page = MainPage(driver)
        username = test_data["username"]
        logged_in_username = main_page.get_logged_in_username(username)
        assert logged_in_username == username, pytest.fail(f"\nExpected: {username}\nBut got: {logged_in_username}")