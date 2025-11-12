# Mobile App Testing with Pytest and Appium

This project provides a framework for testing mobile applications using Pytest and Appium, designed to work with Android Studio emulators or physical devices.

## Prerequisites

1. **Python 3.7+** installed
2. **Android Studio** with Android SDK
3. **Appium Server** installed and running
4. **Java JDK** (required for Appium)
5. **Node.js** (for Appium installation)

## Setup

1. **Clone or download this project**

2. **Create a virtual environment:**
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Install Appium:**
   ```
   npm install -g appium
   appium driver install uiautomator2
   ```

5. **Set up Android device/emulator:**
   - Open Android Studio
   - Create or start an Android Virtual Device (AVD)
   - Note the device name (e.g., emulator-5554)

6. **Prepare your APK:**
   - Place your APK file in the project root directory as `app.apk`
   - Update `conftest.py` with your app's package name and main activity

7. **Update configuration:**
   - In `conftest.py`, update the desired capabilities:
     - `platformVersion`: Your Android version
     - `deviceName`: Your device/emulator name
     - `appPackage`: Your app's package name
     - `appActivity`: Your app's main activity

## Running Tests

1. **Start Appium Server:**
   ```
   appium
   ```

2. **Start your Android emulator or connect a physical device**

3. **Run the tests:**
   ```
   pytest tests/ -v --html=report.html
   ```

## Project Structure

```
├── conftest.py          # Appium driver configuration
├── requirements.txt     # Python dependencies
├── tests/
│   └── test_mobile_app.py  # Sample test cases
├── README.md            # This file
└── app.apk              # Your APK file (add manually)
```

## Writing Tests

Tests use standard Pytest fixtures. The `driver` fixture provides an Appium WebDriver instance, and `wait` provides a WebDriverWait for synchronization.

Example:
```python
def test_my_feature(driver, wait):
    # Your test code here
    element = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example:id/element")))
    assert element.is_displayed()
```

## Troubleshooting

- Ensure Appium server is running on port 4723
- Check that your device/emulator is connected: `adb devices`
- Verify APK path and app details in `conftest.py`
- For physical devices, enable USB debugging in developer options

## Generating Reports

Run tests with HTML reporting:
```
pytest tests/ --html=report.html
```

Open `report.html` in your browser to view detailed test results.
