
from unittest import TestCase
from .home.atieno.Downloads.Stock-Management-System-main.Stock.forms import StockCreateForm, FacilityCreateForm, ClientCreateForm, StockSearchForm, FacilitySearchForm, PatientSearchForm, StockIssuedSearchForm, ReportSearchForm, StockUpdateForm, FacilityUpdateForm, ClientUpdateForm, IssueForm


class TestStockCreateForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.stock_createform = StockCreateForm()
    
    
    def test_clean_item_name(self):
        
        actual_result = self.stock_createform.clean_item_name()
        expected_result = None
        self.assertEqual(actual_result, expected_result)
    
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestFacilityCreateForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.facility_createform = FacilityCreateForm()
    
    
    def test_clean_item_name(self):
        
        actual_result = self.facility_createform.clean_item_name()
        expected_result = None
        self.assertEqual(actual_result, expected_result)
    
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestClientCreateForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.client_createform = ClientCreateForm()
    
    
    def test_clean_item_name(self):
        
        actual_result = self.client_createform.clean_item_name()
        expected_result = None
        self.assertEqual(actual_result, expected_result)
    
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestStockSearchForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.stock_searchform = StockSearchForm()
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestFacilitySearchForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.facility_searchform = FacilitySearchForm()
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestPatientSearchForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.patient_searchform = PatientSearchForm()
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestStockIssuedSearchForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.stock_issuedsearchform = StockIssuedSearchForm()
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestReportSearchForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.report_searchform = ReportSearchForm()
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestStockUpdateForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.stock_updateform = StockUpdateForm()
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestFacilityUpdateForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.facility_updateform = FacilityUpdateForm()
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestClientUpdateForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.client_updateform = ClientUpdateForm()
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestIssueForm(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.issue_form = IssueForm()
    
    def tearDown(self):
        """ Destroy objects after each test """
