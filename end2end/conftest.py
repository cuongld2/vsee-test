import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setUp():
    options = Options()
    # options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # # Bypass OS security model
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_argument("--start-fullscreen")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--user-data-dir=/home/donald/.config/google-chrome/Profile 1')

    return webdriver.Chrome(options=options)
    # self.driver = webdriver.Firefox()
    # self.driver.get("http://www.amazon.com")

def tearDown(driver):
    driver.close()

@pytest.fixture(autouse=True)
def browser_init():
    driver = setUp()
    yield driver
    tearDown(driver)


    