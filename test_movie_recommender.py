import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from scraperFunctions import fetchData, extractData, printData
from mlFunctions import extract_genre_names, recommend

class TestScraperFunctions(unittest.TestCase):
    @patch('scraperFunctions.requests.get')
    def test_fetchData(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = '<html><body>Test</body></html>'
        mock_get.return_value = mock_response

        result = fetchData('http://test.com')
        self.assertIsInstance(result, BeautifulSoup)

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
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['title'], 'Test Movie')
        self.assertEqual(result[0]['description'], 'Test Description')
        self.assertEqual(result[0]['score'], '8.5')

    @patch('builtins.print')
    def test_printData(self, mock_print):
        movies = [{'title': 'Test Movie', 'description': 'Test Description', 'score': '8.5'}]
        printData(movies, "TEST HEADER")
        mock_print.assert_called()

class TestMLFunctions(unittest.TestCase):
    def test_extract_genre_names(self):
        genre_list = '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}]'
        result = extract_genre_names(genre_list)
        self.assertEqual(result, 'Action, Adventure')

    def test_recommend(self):
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
        movies_df = pd.DataFrame(movies_data)

        similarity = np.array([
            [1, 0.9, 0.1, 0.4, 0.6],  # Movie A
            [0.9, 1, 0.2, 0.3, 0.5],   # Movie B
            [0.1, 0.2, 1, 0.6, 0.3],   # Movie C
            [0.4, 0.3, 0.6, 1, 0.7],   # Movie D
            [0.6, 0.5, 0.3, 0.7, 1]    # Movie E
        ])

        with patch('builtins.print') as mock_print:
            recommend('Movie A', movies_df, similarity)
            mock_print.assert_any_call('Movie B')  # expecting movie B and E to be recommended, top 2 similarities
            mock_print.assert_any_call('Movie E')

if __name__ == '__main__':
    unittest.main()