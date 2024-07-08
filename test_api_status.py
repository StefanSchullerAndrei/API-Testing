import unittest
from Simple_books_request import SimpleBooksRequest


class TestApiStatus(unittest.TestCase):
    def setUp(self):
        self.books_api = SimpleBooksRequest()

    def test_api_status(self):
        response = self.books_api.get_api_status()
        # print(response)
        actual_code_response = response.status_code
        expected_response_code = 200
        assert actual_code_response is expected_response_code, f"Expected code:{expected_response_code}, actual code: {actual_code_response}"

