from .pages.product_page import ProductPage
from .pages.product_page import BasePage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest
import time


@pytest.mark.need_review
@pytest.mark.parametrize('stranica', ["0", "1", "2", "3","4","5","6", pytest.param("7", marks=pytest.mark.xfail),"8","9"])
def test_guest_can_add_product_to_basket(browser, stranica):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{stranica}"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.gest_can_add_a_product_to_the_busket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.check_book_name()
    page.check_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.gest_can_add_a_product_to_the_busket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.gest_can_add_a_product_to_the_busket()
    page.should_be_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
      link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
      page = BasePage(browser, link)
      page.open()
      page.open_basket()
      page = BasketPage(browser, link)
      page.check_that_busket_empty()
      page.check_that_busket_does_not_have_books()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        page = LoginPage(browser, link)
        email = str(time.time()) + "@fakemail.org"
        password = "qweQWE0123"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_client_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def  test_client_can_add_product_to_basket(self, browser):
         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
         page = ProductPage(browser, link)
         page.open()
         page.gest_can_add_a_product_to_the_busket()
         page.check_book_name()
         page.check_price()

