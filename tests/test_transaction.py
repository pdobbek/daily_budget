import unittest
from unittest.mock import patch
from core.transaction import Transaction


class TestTransaction(unittest.TestCase):
    @patch('requests.get')
    def test_convert_eur_to_gbp(self, mock_get):
        # Mock API response
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'rates': {'GBP': 0.85}}  # Example rate

        transaction = Transaction("Test", 100, currency="EUR")
        self.assertEqual(transaction.amount, 85.0)  # 100 EUR * 0.85 GBP/EUR = 85 GBP

    def test_convert_gbp_to_gbp(self):
        transaction = Transaction("Test", 100, currency="GBP")
        self.assertEqual(transaction.amount, 100)

    def test_invalid_currency(self):
        with self.assertRaises(NotImplementedError):
            Transaction("Test", 100, currency="USD")  # Should raise an error for unsupported currency
