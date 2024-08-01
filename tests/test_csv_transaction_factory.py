import unittest
from core.transaction_factories import CSVTransactionFactory


class TestCSVTransactionFactory(unittest.TestCase):

    def test_create_transaction(self):
        factory = CSVTransactionFactory()
        data = {'name': 'Test Transaction', 'amount': '100.00', 'day': '15', 'currency': 'GBP'}
        transaction = factory.create_transaction(data)
        self.assertEqual(transaction.name, 'Test Transaction')
        self.assertEqual(transaction.amount, 100.00)
        self.assertEqual(transaction.day, 15)
        self.assertEqual(transaction.currency, 'GBP')

    def test_load_transactions_from_csv(self):
        factory = CSVTransactionFactory()
        transactions = factory.load_transactions_from_csv("../data/test_data.csv")
        self.assertEqual(len(transactions), 6)
        self.assertEqual("Accom.", transactions[0].name)
        self.assertEqual(300, transactions[0].amount)
        self.assertEqual(15, transactions[0].day)
        self.assertEqual("Gym", transactions[1].name)
        self.assertEqual(30, transactions[1].amount)
        self.assertEqual(15, transactions[1].day)
        self.assertEqual("Phone", transactions[2].name)
        self.assertEqual(30, transactions[2].amount)
        self.assertEqual(15, transactions[2].day)
        self.assertEqual("Subs.", transactions[3].name)
        self.assertEqual(20, transactions[3].amount)
        self.assertEqual(15, transactions[3].day)
        self.assertEqual("Air ticket", transactions[4].name)
        self.assertEqual(700, transactions[4].amount)
        self.assertIsNone(transactions[4].day)
        self.assertEqual("Concert", transactions[5].name)
        self.assertEqual(100, transactions[5].amount)
        self.assertIsNone(transactions[5].day)


if __name__ == '__main__':
    unittest.main()
