import json


class ExchangeRateService:
    """Service for getting exchange rate data."""

    def get_exchange_rate(self, eur):
        # Simulating a response from an external exchange rate API
        eur_to_usd = {
            "currency": "USD",
            "rate": 1.1 * eur,
            "timestamp": "2025-04-07T10:00:00"
        }
        eur_to_pound = {
            "currency": "GBP",
            "rate": 0.85 * eur,
            "timestamp": "2025-04-07T10:00:00"
        }
        eur_to_yen = {
            "currency": "YEN",
            "rate": 160 * eur,
            "timestamp": "2025-04-07T10:00:00"
        }
        return eur_to_usd, eur_to_pound, eur_to_yen


# The Facade class


class RateFacade:
    """Facade class to simplify access to the different rate services."""

    def __init__(self):
        self.exchange_rate_service = ExchangeRateService()

    def get_exchange_rate(self, number):
        # Get exchange rate information from the service
        rate_data = self.exchange_rate_service.get_exchange_rate(number)
        return json.dumps(rate_data, indent=4)

# Client code


def main():
    facade = RateFacade()

    # Simulate getting exchange rate data
    print("Exchange Rate JSON:")
    print(facade.get_exchange_rate(100))


if __name__ == "__main__":
    main()
