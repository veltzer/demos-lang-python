"""
This is an example of how to open gmail (real one with session) using selenium.
"""
# import os.path
import time

# from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


options = Options()
# options.add_argument('--headless')  # do not really open a window
# user_data_dir = os.path.expanduser("~/.config/google-chrome/Default")
# user_data_dir = os.path.expanduser("~/.config/google-chrome")
# # assert os.path.isdir(user_data_dir)
# print(user_data_dir)
# options.add_argument(f"--user-data-dir={user_data_dir}")
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
# driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = Firefox(service=Service(GeckoDriverManager().install()), options=options)
driver.get("https://mail.google.com")
time.sleep(10)
