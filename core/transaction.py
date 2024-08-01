import requests


class Transaction:
    def __init__(self, name: str, amount: float, day=None, currency: str = "GBP"):
        self.name = name
        self.amount = self.convert_to_gbp(amount, currency)
        self.currency = "GBP"
        self.day = day

    @staticmethod
    def convert_to_gbp(amount: float, currency: str) -> float:
        """Converts an amount from one currency to another.
        :raise: NotImplemented
        :raise: HTTPError
        """
        if currency == "GBP":
            return amount
        elif currency != "EUR":
            raise NotImplementedError("Unsupported or invalid currency")

        url = "https://api.exchangerate-api.com/v4/latest/EUR"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        gbp_rate = data['rates']['GBP']
        return amount * gbp_rate


if __name__ == "__main__":
    transaction = Transaction("Test", 100, 15, currency="EUR")
    print(transaction.amount, transaction.currency)
