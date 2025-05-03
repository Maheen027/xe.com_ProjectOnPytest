# import pytest
# from selenium import webdriver
# from pages.home_page import HomePage  # Adjust the import path if needed

# @pytest.fixture
# def driver():
#     """Setup and teardown for the browser driver."""
#     driver = webdriver.Chrome()  # Or your preferred browser
#     yield driver
#     driver.quit()

# @pytest.fixture
# def home_page(driver):
#     """Fixture to initialize the HomePage object."""
#     return HomePage(driver)
# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH
    driver.maximize_window()
    yield driver
    # Tear down the browser after the test
    driver.quit()

