

from selenium import webdriver
from pages.login_page import LoginPage
from pages.inbox_page import InboxPage
from selenium import webdriver
import os


def test_send_email(browser_init : webdriver):
    from dotenv import load_dotenv
    load_dotenv()
    LoginPage(browser_init).login(os.getenv('GMAIL_ACCOUNT'),os.getenv('GMAIL_PASSWORD'))
    InboxPage(browser_init).compose()
