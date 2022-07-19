import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# Selenium Class that enables me to use Keyboard Shortcuts such as CTRL+C, SHIFT+ALT etc.
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:\Program Files (x86)\Google\Chrome\Application"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# This will instantiate the webdriver class to use Chrome 
driver = webdriver.Chrome(options=options)

driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=account/register')

driver.implicitly_wait(10)

driver.get('https://demo.seleniumeasy.com/test/basic-first-form-demo.html')
# TO CATCH A POPUP SUCH THAT IT DOES NOT INTERFERE WITH THE TEST
try:
    no_popup = driver.find_element_by_id("popupid")
    no_popup.click()
except:
    print("No popup found..Skip it")

sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, "sum2")

sum1.send_keys(Keys.NUMPAD1,Keys.NUMPAD5)
sum2.send_keys(Keys.NUMPAD2, Keys.NUMPAD0)

# # REGISTRATION TO THE ECOMMERCE WEBSITE
# fname = driver.find_element(By.ID, 'input-firstname')
# lname = driver.find_element(By.ID, 'input-lastname')
# email = driver.find_element(By.ID, 'input-email')
# telephone = driver.find_element(By.ID, 'input-telephone')
# password = driver.find_element(By.ID, 'input-password')
# password_confirm = driver.find_element(By.ID, 'input-confirm')
# subscribe = driver.find_element(By.ID, 'input-newsletter-no')
# privacy = driver.find_element(By.ID, 'input-agree')

