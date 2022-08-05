"""
A simple example of how to use selenium

References:
- https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
- https://stackoverflow.com/questions/16180428/can-selenium-webdriver-open-browser-windows-silently-in-background
"""

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org")
print(driver.title)
