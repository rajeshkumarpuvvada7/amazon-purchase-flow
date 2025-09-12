import pytest
import time

from selenium.webdriver.chrome.webdriver import WebDriver

from amazon_purchase_flow.pages.homepage import HomePage


@pytest.mark.usefixtures("driver")
class TestHomePage:
    driver: WebDriver

    def test_select_dropdown(self):
        home = HomePage(self.driver)
        selected_text = home.select_books_dropdown()
        time.sleep(2)
        assert selected_text == "Books"

    def test_search_book_item(self):
        home = HomePage(self.driver)
        home.search_python_books()
        time.sleep(2)
        assert "Python" in self.driver.title

    @pytest.mark.dependency()
    def test_search_book(self):
        home = HomePage(self.driver)
        home.open_python_programming_book()
        time.sleep(5)
        home.add_book_to_cart()
        time.sleep(5)
