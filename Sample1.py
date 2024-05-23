from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Firefox WebDriver
driver = webdriver.Firefox()

try:
    # Navigate to Google's homepage
    driver.get("https://www.google.com")

    # Allow the page to load
    time.sleep(2)

    # Find the search bar element by its name attribute
    search_box = driver.find_element(By.NAME, "q")

    # Enter "Chatgpt" in the search bar
    search_box.send_keys("Selenium")

    # Press Enter
    search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds to see the results
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()
