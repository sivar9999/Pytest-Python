import pytest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def driver():
    # Desired capabilities for Android Gmail app
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "16",  # Adjust based on your device/emulator
        "deviceName": "emulator-5554",  # Adjust based on your device/emulator
        "automationName": "UiAutomator2",
        "appPackage": "com.google.android.gm",  # Gmail app package
        "appActivity": "com.google.android.gm.ConversationListActivityGmail",  # Main activity
        "noReset": True,
        "fullReset": False
    }

    # Initialize the driver
    driver = webdriver.Remote("http://localhost:4723", desired_caps)

    yield driver

    # Teardown
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
