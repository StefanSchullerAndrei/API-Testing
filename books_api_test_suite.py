import unittest

import HtmlTestRunner

from test_api_status import TestApiStatus
from test_get_all_books import TestGetAllBooks

class TestSuite(unittest.TestCase):
    suita_teste = unittest.TestSuite()

    suita_teste.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(TestApiStatus),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAllBooks)
    ])

    runner = HtmlTestRunner.HTMLTestRunner(
        combine_reports=True,
        report_title= 'Api test report',
        report_name= 'Books API Test Results'
    )
    runner.run(suita_teste)