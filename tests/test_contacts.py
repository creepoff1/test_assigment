from BaseClass import BaseTest
from tests.PageObject.contacts_page import ContactsPage
from tests.PageObject.main_page import MainPage

class TestContacts(BaseTest):

    def test_contacts_title_presented(self, driver):
        main_page = MainPage(driver)
        title = "Контакты"
        main_page.click_contacts_link()
        contacts_page = ContactsPage(driver)
        assert title == contacts_page.check_presence_of_title_on_page(title)
        contacts_page.click_to_back_to_main()