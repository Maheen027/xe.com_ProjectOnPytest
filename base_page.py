from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        """Wait until the element located by `locator` is visible."""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Wait until the element located by `locator` is clickable."""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click_element(self, locator, timeout=10):
        """Wait until the element is clickable and then click it."""
        element = self.wait_for_element_to_be_clickable(locator, timeout)
        element.click()

    def get_element_text(self, locator, timeout=10):
        """Get text from an element after waiting for it to be visible."""
        element = self.wait_for_element(locator, timeout)
        return element.text

    def get_element_attribute(self, locator, attribute, timeout=10):
        """Get an attribute from an element after waiting for it to be visible."""
        element = self.wait_for_element(locator, timeout)
        return element.get_attribute(attribute)

    def get_current_url(self):
        """Get the current URL of the browser."""
        return self.driver.current_url

    def navigate_to(self, url):
        """Navigate to a specific URL."""
        self.driver.get(url)

    def wait_for_url_change(self, old_url, timeout=10):
        """Wait for the current URL to change from `old_url`."""
        WebDriverWait(self.driver, timeout).until(EC.url_changes(old_url))
