"""
This is an example of how to open gmail (real one with session) using selenium.

Turns out this is a really hard thing to do since google really don't want someone
to open gmail in selenium.

I tried with both firefox and chrom (see below) but to no avail.
"""
import os.path
import time

from selenium.webdriver import Chrome, Firefox
import selenium.webdriver.chrome
import selenium.webdriver.firefox
import selenium.webdriver.chrome.options
import selenium.webdriver.firefox.options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


browser = "chrome"
if browser == "chrome":
    options = selenium.webdriver.chrome.options.Options()
    options.add_argument('--headless')  # do not really open a window
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    user_data_dir = os.path.expanduser("~/.config/google-chrome/Default")
    user_data_dir = os.path.expanduser("~/.config/google-chrome")
    assert os.path.isdir(user_data_dir)
    print(user_data_dir)
    options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_driver = Chrome(
        service=selenium.webdriver.chrome.service.Service(ChromeDriverManager().install()),
        options=options,
    )
    chrome_driver.get("https://mail.google.com")
    time.sleep(10)

if browser == "firefox":
    firefox_options = selenium.webdriver.firefox.options.Options()
    firefox_driver = Firefox(
        service=selenium.webdriver.firefox.service.Service(GeckoDriverManager().install()),
        options=firefox_options,
    )
    firefox_driver.get("https://mail.google.com")
    time.sleep(10)
