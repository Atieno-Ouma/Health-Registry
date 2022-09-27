
from unittest import TestCase
from .home.atieno.Downloads.Stock-Management-System-main.Stock.admin import StockCreateAdmin


class TestStockCreateAdmin(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.stock_createadmin = StockCreateAdmin()
    
    def tearDown(self):
        """ Destroy objects after each test """
