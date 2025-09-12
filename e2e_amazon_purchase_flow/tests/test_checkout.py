import pytest
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from amazon_purchase_flow.pages.test_checkout import CheckoutPage


@pytest.mark.dependency(depends=["TestHomePage::test_search_book_item"])
@pytest.mark.usefixtures("driver")
class TestCheckoutPage:
    driver: WebDriver

    def test_cart_page(self):
        checkout = CheckoutPage(self.driver)
        checkout.go_to_cart()
        time.sleep(3)
        checkout.proceed_to_checkout()
        text = checkout.get_continue_button_text()
        assert text == "Continue", f"Expected 'Continue' but got '{text}'"
