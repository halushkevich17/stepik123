from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage(BasePage):
    def gest_can_add_a_product_to_the_busket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        time.sleep(1)

    def check_book_name(self):
        time.sleep(2)
        book = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        a = book.text
        book_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET)
        b = book_basket.text
        assert a == b, "book name does not match"

    def check_price(self):
        time.sleep(2)
        cost = self.browser.find_element(*ProductPageLocators.PRICE_COST)
        cost_basket = self.browser.find_element(*ProductPageLocators.PRICE_COST_BASKET)
        assert cost.text == cost_basket.text, "price does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared"










