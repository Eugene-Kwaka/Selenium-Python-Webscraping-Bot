import os

from requests import options
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager


# import the BookingFiltration class that will be instantiated here
from booking.booking_filtrations import BookingFiltration


# The bot project will have the option to inherit from either the webdriver.Chrome class or current Booking Class methods.
class Booking(webdriver.Firefox):
    # The "driver_path" will store the info about the location of the drivers
    # To extend the option of when to we want to tear down the browser or NOT, I include it as an argument whose default it False
    # r"C:\Program Files (x86)\Google\Chrome\Application"
    def __init__(self, driver_path=r"C:\Program Files (x86)\Mozilla Firefox", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown

        os.environ['PATH'] += self.driver_path

        # I need to add some additional options to the class webdriver.chrome class the Booking() class inherits.
        options = webdriver.FirefoxOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # The "super()" is to instantiate the webdriver.Chrome class
        # The constructor is going to complain about how the inherited class is not instantiated yet hence we use super()
        # Super will receive the current Booking Class as an argument and "self" object. Then I will call the __init__ method
        super(Booking, self).__init__(options=options)
        
        # Lets me wait for some time(secs) before an element can be interacted on in a webpage
        # Works on all elements hit with a 'find_element()' method
        self.implicitly_wait(15)
        self.maximize_window()

    # This context manager releases the resources occupied with the current code snippet containing the keyword "with"
    def __exit__(self, exc_type, exc_value, exc_tb):
        # If teardwon is True then the browser will be shutdown by this context manager
        if self.teardown:
            # this method will be responsible to shut down Chrome when done
            self.quit()

    def land_first_page(self):
        # The url is imported from the constants.py file
        self.get(const.BASE_URL)

    # The currency argument default is None
    def change_currency(self, currency=None):
        currency_element =self.find_element(By.CSS_SELECTOR, "button[data-tooltip-text='Choose your currency']")
        currency_element.click()
        # When locating an element with a substring, I use * 
        selected_currency_element = self.find_element(By.CSS_SELECTOR,
        # I will change the element locator to a f string so that I pass in the currency argument
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, "ss")
        # cleaning the existing text in a form input
        search_field.clear()
        # send_keys will input something in the search field.
        # I will use the place_to_go argument here and in the run.py 
        search_field.send_keys(place_to_go)
        # After searching, a couple of locations will show up. These locations are listed by order of their index numbers
        first_result = self.find_element(By.CSS_SELECTOR,
            # Find the first[0] indexed location
            'li[data-i="0"]')
        first_result.click()

    # check_in_date and check_out_date are arguments provided to prevent hard coding the dates in this function
    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR,
            f'td[data-date="{check_in_date}"')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, 
            f'td[data-date="{check_out_date}"')
        check_out_element.click()

    # The count argument is to record the number of clicks to add or subtract the no. of people selected
    # The default number is 1 which represents 1 adult.
    def select_people(self, count=1):
        select_element = self.find_element(By.ID, 'xp__guests__toggle')
        select_element.click()
        # In booking.com the default no.of people(adults) shown is 2.
        # But this number can change anytime and I want to be smart about it.
        # So I write a script that at first decreases the default value to 1, then from that I will automate the clicks to the number of people I want.
        # Simulate the click of this button until the no. of adults is 1. This will give me more control to decide the no of adults I want
        while True:
            decrease_adults_element = self.find_element(By.CSS_SELECTOR,
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()
            # if the value of adults reaches 1, I will get out of this loop.
            # I locate the input that changes once an adult is added or removed by its ID.
            adults_value_element = self.find_element(By.ID, 'group_adults')
            # TO RECEIVE A VALUE OF SOME KEY IN HTML ELEMENT(INPUT), I USE THE GET_ATTRIBUTE() METHOD
            # This will give back the adults count.
            adults_value = adults_value_element.get_attribute('value')
            # If the no. of adults is equal to 1 then break out of the loop
            if int(adults_value) == 1:
                break
        # This button increases the number of adults 
        increase_adults_element = self.find_element(By.CSS_SELECTOR,
            'button[aria-label="Increase number of Adults"]'
        )
        # This forloop gives me control over the amount of times I will click to add in an adult.
        # The range will control how many times the forloop runs 
        # I am decreasing count by 1 to achieve the exact count that is passed in this forloop
        # I am using the _ to show that I am not using any variable to execute the forloop.
        for _ in range(count -1):
            increase_adults_element.click()

    def click_search(self):
        search_button_element = self.find_element(By.CSS_SELECTOR,
            'button[type="submit"]')
        search_button_element.click()


    def apply_filtrations(self):
        # I will instantiate the class and define the driver argument as self.
        # the driver argument will relate to the BookingFiltration class 
        filtration = BookingFiltration(driver=self)
        # Since this method references to the BookingFiltration class, I have to instantiate the apply_star_rating it from here
        # I specify the star value I want the bot to click
        filtration.apply_star_rating(4)
        filtration.sort_price_lowest_first()
