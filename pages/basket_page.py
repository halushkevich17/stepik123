from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasketPage(BasePage):
    def check_that_busket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BUSKET_EMPTY), \
            "Busket not empty"

    def check_that_busket_does_not_have_books(self):
        assert self.is_not_element_present(*BasketPageLocators.BUSKET_BOOKS),\
        "Busket has books"