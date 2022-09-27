
from unittest import TestCase
from .home.atieno.Downloads.Stock-Management-System-main.Stock.widget import DatePickerInput, TimePickerInput, DateTimePickerInput


class TestDatePickerInput(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.date_pickerinput = DatePickerInput()
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestTimePickerInput(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.time_pickerinput = TimePickerInput()
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestDateTimePickerInput(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.date_timepickerinput = DateTimePickerInput()
    
    def tearDown(self):
        """ Destroy objects after each test """
