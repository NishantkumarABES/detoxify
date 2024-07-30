from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to your ChromeDriver executable
CHROMEDRIVER_PATH = '/path/to/chromedriver'

# Path to your extension directory
EXTENSION_PATH = '/path/to/your/extension/folder'

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument(f'load-extension={EXTENSION_PATH}')

# Initialize ChromeDriver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open YouTube or any other page where you want to test the extension
driver.get('https://www.youtube.com/')

# Wait for the page to load
time.sleep(5)  # Adjust sleep time as needed

# Interact with the extension's popup
# For example, click the extension icon and test functionality
# Locate and interact with elements in the extension popup if needed

# Example: Locate the extension icon and click it (adjust selector as needed)
# driver.find_element_by_id('extension-icon-id').click()

# Wait and perform tests
time.sleep(10)  # Adjust sleep time as needed for testing

# Clean up
driver.quit()