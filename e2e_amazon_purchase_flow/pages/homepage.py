from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    dropdown_id = "searchDropdownBox"
    search_box_id = "twotabsearchtextbox"
    search_button_id = "nav-search-submit-button"
    book_xpath = "//span[text()='PYTHON PROGRAMMING, 3E']"
    add_to_cart_id = "a-autoid-2-announce"

    # Actions
    def select_books_dropdown(self):
        dropdown = Select(self.driver.find_element(By.ID, self.dropdown_id))
        dropdown.select_by_visible_text("Books")
        return dropdown.first_selected_option.text

    def search_python_books(self, text="Python"):
        self.driver.find_element(By.ID, self.search_box_id).send_keys(text)
        self.driver.find_element(By.ID, self.search_button_id).click()

    def open_python_programming_book(self):
        self.driver.find_element(By.XPATH, self.book_xpath).click()

    def add_book_to_cart(self):
        self.driver.find_element(By.ID, self.add_to_cart_id).click()
