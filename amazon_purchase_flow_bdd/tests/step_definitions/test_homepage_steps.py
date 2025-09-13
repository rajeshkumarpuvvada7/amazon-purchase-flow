import time
import pytest
from pytest_bdd import scenarios, given, when, then

from amazon_purchase_flow_bdd.pages.homepage import HomePage

# relative import

scenarios("../features/homepage.feature")


@pytest.fixture
def home(driver):
    return HomePage(driver)


@given("I am on the Amazon homepage")
def open_homepage(driver):
    driver.get("https://www.amazon.in/")


@when('I search for "Iphone"')
def search_phone(home):
    home.search_phone_mobiles("iphone 16")
    time.sleep(2)


@when("Click Search button")
def search_button(home):
    home.click_search_icon()


@when("Go to cart")
def go_to_cart(home):
    home.go_to_cart()


@when("click delete hyperlink for mobile")
def delete_link(home):
    home.delete_mobile()


@when("Add phone to cart")
def add_phone_to_cart(home):
    home.add_phone_to_cart()


@then("validate text after delete mobile")
def validate_text_after_delete_item(home):
    home.validate_text_after_delete()
