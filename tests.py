from unittest import TestCase, mock
from io import StringIO
import sys
import logging

from main import fetch_data_from_api, create_users_table, insert_data_into_users_table, verify_data

class ScriptTestCase(TestCase):
    def setUp(self):
        self.mock_conn = mock.MagicMock()

    def test_fetch_data_from_api_success(self):
        """
        Test the fetch_data_from_api function for successful API data retrieval.

        This test mocks the HTTP GET request to the API and ensures that the returned data
        matches the expected data.
        """
        expected_data = [{'name': 'John', 'surname': 'Doe', 'country': 'USA', 'gender': 'Male'}]
        mock_response = mock.Mock()
        mock_response.json.return_value = expected_data
        with mock.patch('requests.get', return_value=mock_response):
            data = fetch_data_from_api()
        self.assertEqual(data, expected_data)

    def test_create_users_table_success(self):
        """
        Test the create_users_table function for successful creation of the users table.

        This test verifies that the SQL query executed matches the expected query for creating
        the users table.
        """
        mock_cursor = self.mock_conn.cursor.return_value
        create_users_table(mock_cursor)
        mock_cursor.execute.assert_called_once_with('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                country TEXT,
                name TEXT,
                surname TEXT,
                gender TEXT,
                UNIQUE(name, surname)
            )
        ''')
        
    def test_verify_data_success(self):
        """
        Test the verify_data function for successful verification of data.

        This test captures the output of the function and compares it with the expected output.
        It ensures that the verified data matches the expected format.
        """
        mock_cursor = self.mock_conn.cursor.return_value
        expected_output = "(1, 'USA', 'John', 'Doe', 'Male')\n"  # Add \n at the end
        mock_stdout = StringIO()
        with mock.patch('sys.stdout', mock_stdout):
            verify_data(mock_cursor)
        self.assertEqual(mock_stdout.getvalue(), expected_output)