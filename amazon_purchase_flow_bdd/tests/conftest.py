import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # You can use Chrome, Firefox, or Edge depending on what you installed
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
