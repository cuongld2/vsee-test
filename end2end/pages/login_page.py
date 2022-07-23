
from time import sleep
import time
from utils.locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)  # Python2 version

    def enter_email(self, email):
        self.wait_element(*self.locator.EMAIL)
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.wait_element(*self.locator.PASSWORD)
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_email_next(self):
        self.wait_element(*self.locator.EMAIL_NEXT)
        self.find_element(*self.locator.EMAIL_NEXT).click()
    
    def click_password_next(self):
        self.wait_element(*self.locator.PASSWORD_NEXT)
        self.find_element(*self.locator.PASSWORD).click()

    def login(self, email, password):
        self.enter_email(email)
        self.click_email_next()
        self.enter_password(password)
        self.click_password_next()
