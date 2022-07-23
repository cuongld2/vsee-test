from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
    LOGO = (By.ID, 'nav-logo')
    ACCOUNT = (By.ID, 'nav-link-accountList')
    SIGNUP = (By.CSS_SELECTOR, '#nav-signin-tooltip > div > a')
    LOGIN = (By.CSS_SELECTOR, '#nav-signin-tooltip > a')
    SEARCH = (By.ID, 'twotabsearchtextbox')
    SEARCH_LIST = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')


class LoginPageLocators(object):
    EMAIL = (By.ID, 'identifierId')
    PASSWORD = (By.NAME, 'password')
    EMAIL_NEXT = (By.ID, 'identifierNext')
    PASSWORD_NEXT = (By.CSS_SELECTOR, '#passwordNext > div > button')


class InboxPageLocators(object):
    COMPOSE = (By.CSS_SELECTOR,'[jscontroller="eIu7Db"]')