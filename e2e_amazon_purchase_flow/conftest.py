import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Edge()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    request.cls.driver = driver  # attach driver to the class
    yield
    driver.quit()
