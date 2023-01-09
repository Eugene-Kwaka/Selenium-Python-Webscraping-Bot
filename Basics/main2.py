import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# Selenium Class that enables me to use Keyboard Shortcuts such as CTRL+C, SHIFT+ALT etc.
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:\SeleniumDrivers"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# This will instantiate the webdriver class to use Chrome 
driver = webdriver.Chrome(options=options)

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

driver.implicitly_wait(5)

# TO CATCH A POPUP SUCH THAT IT DOES NOT INTERFERE WITH THE TEST
try:
    no_popup = driver.find_element(By.ID, "popupid")
    no_popup.click()
except:
    print("No popup found..Skipping it")

# Locate the input form to enter the numbers for addition
sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, 'sum2')

sum1.send_keys(Keys.NUMPAD1,Keys.NUMPAD5)
sum2.send_keys(Keys.NUMPAD2, Keys.NUMPAD0)

# Click on the Get Total Button to display the result
get_total = driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
get_total.click()

# display result
result = driver.find_element(By.CSS_SELECTOR, 'span[id="displayvalue"]')
# Prints the result
print("The sum is: ", result.text)

driver.quit()


