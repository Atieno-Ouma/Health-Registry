
from unittest import TestCase
from .home.atieno.Downloads.Stock-Management-System-main.Stock.models import Stock, Client, Facility, Stock_Issued


class TestStock(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.stock = Stock()
    
    
    def test___str__(self):
        
        actual_result = self.stock.__str__()
        expected_result = None
        self.assertEqual(actual_result, expected_result)
    
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestClient(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.client = Client()
    
    
    def test___str__(self):
        
        actual_result = self.client.__str__()
        expected_result = None
        self.assertEqual(actual_result, expected_result)
    
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestFacility(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.facility = Facility()
    
    
    def test___str__(self):
        
        actual_result = self.facility.__str__()
        expected_result = None
        self.assertEqual(actual_result, expected_result)
    
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestStock_Issued(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.stock__issued = Stock_Issued()
    
    def tearDown(self):
        """ Destroy objects after each test """
