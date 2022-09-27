
from unittest import TestCase
from .home.atieno.Downloads.Stock-Management-System-main.Stock.apps import StockConfig


class TestStockConfig(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.stock_config = StockConfig()
    
    def tearDown(self):
        """ Destroy objects after each test """
