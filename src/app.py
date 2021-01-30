import unittest

from utils.log import set_logging_config
from tests.search_text import SearchText
from tests.home_page_test import HomePageTest

def app() -> None:
    set_logging_config()
    
    # get all tests from SearchText and HomePageTest class
    search_text_tests = unittest.TestLoader().loadTestsFromTestCase(SearchText)
    home_page_test_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
    
    # create a test suite combining search_text and home_page_tes
    test_suite = unittest.TestSuite([home_page_test_tests, search_text_tests])
    
    # run the suite
    unittest.TextTestRunner(verbosity=2).run(test_suite)

if __name__ == "__main__":
    app()
