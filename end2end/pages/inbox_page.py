
import time
from utils.locators import *
from pages.base_page import BasePage


class InboxPage(BasePage):
    def __init__(self, driver):
        self.locator = InboxPageLocators
        super(InboxPage, self).__init__(driver)  # Python2 version

    def compose(self,):
        self.wait_element(*self.locator.COMPOSE)
        self.find_element(*self.locator.COMPOSE).click()
        time.sleep(3)