from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    cart_icon_id = "nav-cart-count-container"
    proceed_button_name = "proceedToRetailCheckout"
    continue_button_id = "continue"

    # Actions
    def go_to_cart(self):
        self.driver.find_element(By.ID, self.cart_icon_id).click()

    def proceed_to_checkout(self):
        self.driver.find_element(By.NAME, self.proceed_button_name).click()

    def get_continue_button_text(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.continue_button_id))
        )
        return continue_button.text
