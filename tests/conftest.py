import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.PageObject.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def test_data():
    return {
        "email": "bulyginoleg89@gmail.com",
        "username": "Oleg Bulygin",
        "password": "Vfcnth4321Cktqd!",
        "category": "Электроника",
        "subcategory": "Планшеты",
        "subsubcategory": "Digma",
        "product_name": "Планшет Digma iDx10 8Gb"
    }


@pytest.fixture(autouse=True)
def close_modal_if_present(driver):
    try:
        modal_close_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Принять']")))
        modal_close_button.click()
    except Exception as e:
        pass


@pytest.fixture(scope='session', autouse=True)
def login(driver, test_data):
    driver.get("https://mega.readyscript.ru/")
    main_page = MainPage(driver)
    email = test_data["email"]
    password = test_data["password"]

    main_page.click_icon_lk()
    main_page.click_login_link()
    main_page.enter_email(email)
    main_page.enter_password(password)
    main_page.click_login_button()

    username = test_data["username"]
    logged_in_username = main_page.get_logged_in_username(username)
    assert logged_in_username == username, "Login failed!"

    yield main_page

    main_page.click_logout_link()
