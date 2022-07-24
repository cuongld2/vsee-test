from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy,AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    "deviceName": "BKW00043349",
    "platformName": "Android",
    "version" : "11",
    "appPackage": "com.thecoffeehouse.guestapp",
    "appActivity":"com.thecoffeehouse.guestapp.MainActivity",
    "automationName":"Appium"

}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# driver.start_activity(app_package="com.vsee.vsee.beta",app_activity="com.vsee.vsee.beta.MainActivity")
driver.launch_app()
assert "Chào bạn mới" in driver.find_element(by=AppiumBy.ID,value="com.thecoffeehouse.guestapp:id/txt_title_main_header").text
driver.find_element(by=AppiumBy.ID,value="com.thecoffeehouse.guestapp:id/txt_login").click()

driver.quit()