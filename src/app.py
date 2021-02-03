import unittest

from utils.log import set_logging_config
from tests.search_text import SearchText
from tests.home_page_test import HomePageTest

def app() -> None:
    #creates logger in the container
    set_logging_config()

    #discover the test suite
    test_suite = unittest.TestLoader().discover('tests','*test.py','.')
    unittest.TextTestRunner(verbosity=2).run(test_suite)

if __name__ == "__main__":
    app()
