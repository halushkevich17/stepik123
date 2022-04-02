from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class ProductPageLocators():
    BASKET_BUTTON = (By.XPATH, "//button[@value='Add to basket']")
    BOOK_NAME = (By.XPATH, "//h1[text()='Coders at Work']")
    PRICE_COST = (By.XPATH, "//p[text() = '£19.99']")
    BOOK_NAME_BASKET = (By.XPATH, "//strong[text() = 'Coders at Work']")
    PRICE_COST_BASKET =(By.XPATH, "//strong[text() = '£19.99']")
    SUCCESS_MESSAGE =(By.XPATH, "//div[@id='messages']/div[1]")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.XPATH, "//a[text()='View basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BUSKET_EMPTY = (By.XPATH, "//div[@id='content_inner']/p[contains(text(), 'empty')]")
    BUSKET_BOOKS = (By.XPATH, "//h3[text()='Order total']")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_BUTTON = (By.XPATH, "//a[@id='login_link']")
    EMAIL_FIELD = (By.XPATH, "//input[@*='id_registration-email']")
    PASSWORD1_FIELD =(By.XPATH, "//input[@*='registration-password1']")
    PASSWORD2_FIELD = (By.XPATH, "//input[@*='registration-password2']")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[@*='registration_submit']")