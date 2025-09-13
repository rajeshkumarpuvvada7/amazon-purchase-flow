from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    search_box_id = "twotabsearchtextbox"
    search_button_id = "nav-search-submit-button"
    add_to_cart_id = "a-autoid-1-announce"
    cart_icon_id = "nav-cart-count-container"
    delete_link = "//input[@data-feature-id='item-delete-button']"
    text_validate = "//span[@id='sc-subtotal-label-activecart']"

    # Actions

    def search_phone_mobiles(self, text="iphone 16"):
        self.driver.find_element(By.ID, self.search_box_id).send_keys(text)

    def click_search_icon(self):
        self.driver.find_element(By.ID, self.search_button_id).click()

    def add_phone_to_cart(self):
        self.driver.find_element(By.ID, self.add_to_cart_id).click()

    def go_to_cart(self):
        self.driver.find_element(By.ID, self.cart_icon_id).click()

    def delete_mobile(self):
        self.driver.find_element(By.XPATH, self.delete_link).click()

    def validate_text_after_delete(self):
        o_text = self.driver.find_element(By.XPATH, self.text_validate).text.strip().rstrip(':')
        e_text = "Subtotal (0 items)"
        assert o_text == e_text, f'The text is different than expected. Actual: "{o_text}", Expected: "{e_text}"'
