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
        return eur_to_usd


class ExchangeServiceCost:
    """Cost for exchange servise."""

    def get_discount(self, eur):
        # Simulating a response from an external exchange rate API
        eur_to_usd_cost = {
            "current": eur,
            "cost": 0.10,
            "final": eur + 0.10
        }
        return eur_to_usd_cost


class ExchangeLimit:
    """Limit for exchange servise."""

    def get_limit(self):
        # Simulating a response from an external exchange rate API
        eur_to_usd_limit = {
            "limit": 100000
        }
        return eur_to_usd_limit


class RateFacade:
    """Facade class to simplify access to the different rate services."""

    def __init__(self):
        self.exchange_rate_service = ExchangeRateService()
        self.exchange_rate_cost = ExchangeServiceCost()
        self.exchange_limit = ExchangeLimit()

    def get_rates(self, number):
        # Get exchange rate information from the service
        all_rates = {
            "rate_exchange_cost": self.exchange_rate_cost.get_discount(number),
            "rate_exchange": self.exchange_rate_service.get_exchange_rate(
                number),
            "exchange_limit": self.exchange_limit.get_limit()
        }
        return json.dumps(all_rates, indent=4)

# Client code


def main():
    facade = RateFacade()

    # Simulate getting exchange rate data
    print("Exchange Rates EUR TO :")
    print(facade.get_rates(100))


if __name__ == "__main__":
    main()
