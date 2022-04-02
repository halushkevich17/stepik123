from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage(BasePage):

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Link isn't correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
        time.sleep(1)
        field1 = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        field1.send_keys(email)
        time.sleep(1)
        field2 = self.browser.find_element(*LoginPageLocators.PASSWORD1_FIELD)
        field2.send_keys(password)
        time.sleep(1)
        field3 = self.browser.find_element(*LoginPageLocators.PASSWORD2_FIELD)
        field3.send_keys(password)
        time.sleep(1)
        button2 = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        button2.click()
        time.sleep(6)



