from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome WebDriver
options = Options()
options.add_argument("--headless")  # do not really open a window
options.add_argument("--disable-gpu")  # Last I checked this was necessary.
driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the Google homepage
driver.get("https://www.google.com")

# Find the search input element by its name attribute ("q")
search_input = driver.find_element(By.NAME, "q")  # Use By.NAME here

# Enter a search query (e.g., "Selenium testing") into the search input
search_input.send_keys("Selenium testing")

# Submit the search form (press Enter)
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load (you can specify a longer wait time if needed)
driver.implicitly_wait(10)

# Get the page title and assert that it contains the search query
page_title = driver.title
assert "Selenium testing" in page_title

# Close the browser window
driver.quit()
