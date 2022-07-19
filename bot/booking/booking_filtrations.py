# import os
# import booking.constants as const
# from selenium import webdriver
from selenium.webdriver.common.by import By
# this library will enable me to get autocompletion for my driver instance and connect it to my webdriver
from selenium.webdriver.remote.webdriver import WebDriver

# The class will not inherit from the any class
class BookingFiltration():
    # the __init__ constructor method will have one parameter and this parameter is going to be the driver.
    # the driver will be passed in as the argument coz I need to work with the webdriver.
    def __init__(self, driver:WebDriver):
        # this will receive the original driver from the Booking Class
        self.driver = driver

    # The star_value argument is important to show what the star value to filter is (2,3,4,5)
    # Adding the *star_value makes that argument be able to pass in many arguments in it
    def apply_star_rating(self, *star_values):
        # This finds the whole star filtration box as a div
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR,
            'div[data-filters-group="class"]')
        # since I'm looking for child elements of the star_filtration_box
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')
        # looping through multiple star_values
        for star_value in star_values:
            # Iterate over the child elements to find out which one has the star_value substring of 2,3,4,5 or unrated star filter
            for star_element in star_child_elements:
                # Looking for the attribute that is responsible to find the inner text
                # I'm changing the value extracted to a string and using the strip() method to remove white spaces.
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()

    def sort_price_lowest_first(self):
        # sort_by_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-selected-sorter="popularity"]')
        # sort_by_button.click()
        # # this button filters the results by price_lowest-first
        # sort_price_button = self.driver.find_element(By.CSS_SELECTOR,
        #     'button[data-id="price"]'
        # )
        # sort_price_button.click()
        try:
            # This button presents a list dropdown that shows the sort filters
            sort_by_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-selected-sorter="popularity"]')
            sort_by_button.click()
            # this button filters the results by price_lowest-first
            sort_price_button = self.driver.find_element(By.CSS_SELECTOR,
                'button[data-id="price"]'
            )
            sort_price_button.click()
        except:
            sort_price_button = self.driver.find_element(By.CSS_SELECTOR,
                'li[data-id="price"]'
            )
            sort_price_button.click()
