# Unit tests

import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from scraperFunctions import fetchData, extractData, printData
from mlFunctions import extract_genre_names, recommend

# Define a test class for scraper functions
class TestScraperFunctions(unittest.TestCase):
    @patch('scraperFunctions.requests.get')  # Mock the requests.get method
    def test_fetchData(self, mock_get):
        mock_response = MagicMock()  # Create a mock response object
        mock_response.status_code = 200
        mock_response.content = '<html><body>Test</body></html>'
        mock_get.return_value = mock_response  # Return the mock response when requests.get is called

        result = fetchData('http://test.com')
        self.assertIsInstance(result, BeautifulSoup)  # Check if the result is a BeautifulSoup object

    def test_extractData(self):
        mock_html = '''
        <div class="c-finderProductCard">
            <h3 class="c-finderProductCard_titleHeading">Test Movie</h3>
            <div class="c-finderProductCard_description">Test Description</div>
            <div class="c-siteReviewScore">8.5</div>
        </div>
        '''
        soup = BeautifulSoup(mock_html, 'html.parser')
        result = extractData([soup])
        self.assertEqual(len(result), 1)  # Check if one movie was extracted
        self.assertEqual(result[0]['title'], 'Test Movie')  # Verify the title
        self.assertEqual(result[0]['description'], 'Test Description')  # Verify the description
        self.assertEqual(result[0]['score'], '8.5')  # Verify the score

    @patch('builtins.print')  # Mock the print function
    def test_printData(self, mock_print):
        movies = [{'title': 'Test Movie', 'description': 'Test Description', 'score': '8.5'}]  # Create a mock movie list
        printData(movies, "TEST HEADER")
        mock_print.assert_called() 

# Define a test class for machine learning functions
class TestMLFunctions(unittest.TestCase):
    def test_extract_genre_names(self):
        # Test the extract_genre_names function with a mock genre list
        genre_list = '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}]'
        result = extract_genre_names(genre_list)
        self.assertEqual(result, 'Action, Adventure')  # Verify the output

    def test_recommend(self):
        # Create a mock DataFrame for testing recommendations
        movies_data = {
            'id': [1, 2, 3, 4, 5],
            'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
            'tags': [
                'action adventure',    # Movie A
                'action thriller',     # Movie B
                'romance drama',       # Movie C
                'comedy romance',      # Movie D
                'action comedy'        # Movie E
            ]
        }
        movies_df = pd.DataFrame(movies_data)  # Create a DataFrame from the mock data

        # Create a mock similarity matrix
        similarity = np.array([
            [1, 0.9, 0.1, 0.4, 0.6],  # Movie A
            [0.9, 1, 0.2, 0.3, 0.5],   # Movie B
            [0.1, 0.2, 1, 0.6, 0.3],   # Movie C
            [0.4, 0.3, 0.6, 1, 0.7],   # Movie D
            [0.6, 0.5, 0.3, 0.7, 1]    # Movie E
        ])

        with patch('builtins.print') as mock_print:  # Mock the print function
            recommend('Movie A', movies_df, similarity)
            mock_print.assert_any_call('Movie B')  # Check if Movie B was recommended
            mock_print.assert_any_call('Movie E')  # Check if Movie E was recommended


if __name__ == '__main__':
    unittest.main()
