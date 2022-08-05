"""
A simple example of how to use selenium

References:
- https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
- https://stackoverflow.com/questions/16180428/can-selenium-webdriver-open-browser-windows-silently-in-background
- https://stackoverflow.com/questions/46920243/
    how-to-configure-chromedriver-to-initiate-chrome-browser-in-headless-mode-throug
"""

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument('--headless')  # do not really open a window
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.python.org")
print(driver.title)
