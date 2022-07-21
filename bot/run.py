# from booking.py in booking directory, import the Booking class
from booking.booking import Booking

# I want to use the CLI to run the bot, since there are exceptions that might occur, I will use the try & except method.
# One of the exceptions to occur is the webdriver PATH error.
try:
    # Use of CONTEXT MANAGERS
    # context manager keyword "with" instantiating the instance of Booking Class
    # To teardown the chrome browser window after the test execution, I simply include it in the code below
    # with Booking(teardown=True) as bot:
    with Booking() as bot:
        # the bot is the class instance and then instantiates the first method we created
        bot.land_first_page()
        # The currency argument will also be passed in the method below
        bot.change_currency(currency='USD')
        # I will use the place_to_go argument to specify the location the bot searches
        bot.select_place_to_go('Mombasa')
        # Check_out_dates will reference the dates in the booking.py file
        bot.select_dates(check_in_date='2022-07-19', check_out_date='2022-07-23')
        bot.select_people(5)
        bot.click_search()
        bot.apply_filtrations()
        # Check for the number of hotels in the report_deals() method
        print(len(bot.report_results()))

# If the above code raises an exception, execute this code below
except Exception as e:
    # If the error in the terminal has the following substring 'in PATH' then..
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from the CLI \n'
            'Please add to PATH your chromedriver \n'
            'Windows: \n'
            '   set PATH=%PATH%; C:path-to-your-folder \n \n'
            'Linux: \n'
            '   PATH=SPATH:/path/to-your-folder/ \n'
        )
    else:
        # raise the exception if the above code is not the case
        raise