import unittest
from unittest.mock import Mock, patch
import sys
import os
import datetime
from bs4 import BeautifulSoup
# Add the parent directory of 'src' to the Python path
project_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(project_root, 'src'))  # Updated path to 'src'

from crawler import Crawler 

class TestCrawler(unittest.TestCase):

        @patch('crawler.requests.get')
        def test_extract_from_dolar_hoje(self, mock_requests_get):
            # Mock the response from requests.get
            mock_response = Mock()
            mock_response.text = '<html><body><span class="cotMoeda nacional"><input id="nacional" type="text" value="5,32"/></span></body></html>'
            mock_requests_get.return_value = mock_response

            # Create an instance of Crawler
            crawler_instance = Crawler()

            # Call the method to be tested
            crawler_instance.extract_from_dolar_hoje()

            # Check if the extracted data is not None
            self.assertIsNotNone(crawler_instance.dolar_data)

            # Check if the 'value' field is a valid number (float)
            value = crawler_instance.dolar_data['value']
            value = value.replace(',', '.')  # Replace comma with dot
            self.assertTrue(isinstance(float(value), float))  # Convert to float

            # Check if the 'currency' field matches the expected value
            self.assertEqual(crawler_instance.dolar_data['currency'], 'Dólar Americano')

            # Check if the 'time_of_extract' field is a valid datetime string
            self.assertTrue(
                datetime.datetime.strptime(crawler_instance.dolar_data['time_of_extract'], "%Y-%m-%d %H:%M:%S")
            )

if __name__ == '__main__':
    unittest.main()