import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\Program Files (x86)\Google\Chrome\Application"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# This will instantiate the webdriver class to use Chrome 
driver = webdriver.Chrome(options=options)
# Load the specific website we want
driver.get('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
# Add a time frame in seconds to wait so that the website loads completely.
# If the webpage loads before 8 seconds are over, it will still run and I won't have to wait till all the seconds are over
driver.implicitly_wait(8)
# Find the element we want by its ID
myelement = driver.find_element(By.ID, "downloadButton")
# Click the element
myelement.click()

# USING EXPLICIT_WAIT
# I write the condition that I want to wait for to happen.
# I first instantiate the web driver and include the explicit_wait time.
WebDriverWait(driver, 30).until(
    # This condition waits until the expected condition in which the text to be displayed should be in the element
    EC.text_to_be_present_in_element(
        # Locate the element we would like to check the condition on
        (By.CLASS_NAME, 'progress-label'),
        # Text expected to be displayed to have after 30 seconds of wait time.
        'Complete!'
    )
)

driver.quit()