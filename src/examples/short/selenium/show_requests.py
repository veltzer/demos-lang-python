"""
An example showing how you can load a page and see all requests to get that page.

References:
- https://stackoverflow.com/questions/26481212/capture-ajax-response-with-selenium-and-python
"""
import os.path

from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
# dir_user = os.path.expanduser("~/.config/google-chrome/Default")
# options.add_argument(f"user-data-dir={dir_user}")
dir_profile = os.path.expanduser("~/.config/google-chrome/Default")
options.add_argument(f"profile-directory={dir_profile}")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.instagram.com/w.vasabi")
for request in driver.requests:
    if request.response:
        print(
            request.url,
            request.response.status_code,
            request.response.headers['Content-Type']
        )
