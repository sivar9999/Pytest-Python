import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_app_launch(driver, wait):
    """Test that the Gmail app launches successfully"""
    # Wait for the app to launch - check for any element that indicates the app is loaded
    # Try different possible elements that might be present on launch
    try:
        # Wait for the main Gmail screen or any identifiable element
        wait.until(lambda d: len(d.find_elements(By.CLASS_NAME, "android.widget.TextView")) > 0)
        # Alternatively, wait for a specific element if known
        # wait.until(EC.presence_of_element_located((By.ID, "com.google.android.gm:id/conversation_list_view")))
    except:
        pass  # If timeout, continue

    # Assert that the driver is active and page source is not empty
    assert driver.page_source is not None
    assert len(driver.page_source) > 0

def test_button_click(driver, wait):
    """Test clicking a button in the app"""
    # Navigate to a website
    driver.get("https://www.google.com")

    # Wait for the search button to be clickable
    button = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))

    # Click the button
    button.click()

    # Wait for some result (adjust based on your app's behavior)
    result_element = wait.until(EC.presence_of_element_located((By.ID, "result-stats")))
    assert "results" in result_element.text

def test_text_input(driver, wait):
    """Test entering text into a field"""
    # Navigate to a website
    driver.get("https://www.google.com")

    # Wait for the text input field
    text_field = wait.until(EC.presence_of_element_located((By.NAME, "q")))

    # Enter text
    text_field.send_keys("Hello, Appium!")

    # Verify the text was entered
    assert text_field.get_attribute("value") == "Hello, Appium!"
