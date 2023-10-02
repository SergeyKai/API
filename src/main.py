import requests

from preferences import API_KEY


class CurrencyAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.apilayer.com/currency_data/'

    def _make_request(self, endpoint, params=None):
        headers = {
            'apikey': self.api_key,
        }
        payload = {}
        response = requests.get(
            url=self.base_url + endpoint,
            headers=headers,
            data=payload,
            params=params,
        )
        # print(response.url)
        return response

    def get_change(self, start_date, end_date, currencies=None, source=None):
        """
        Change endpoint, you may request the change (both margin and percentage) of one or
        more currencies, relative to
        a Source Currency, within a specific time-frame (optional).

        :param start_date: The start date of your preferred timeframe.
        :param end_date: The end date of your preferred timeframe
        :param currencies: Accepts a list of comma-separated currency codes to limit output currencies.
        :param source: Accepts the three-letter currency code of your preferred source currency.
        :return: JSON or None
        """
        endpoint = 'change'
        params = {
            'start_date': start_date,
            'end_date': end_date,
        }
        response = self._make_request(endpoint, params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Request error. Status code: {response.status_code}')
            return None

    def get_list(self):
        """
        A full list of supported currencies.

        :return: JSON or None
        """
        endpoint = 'list'
        response = self._make_request(endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            print(f'Request error. Status code: {response.status_code}')
            return None

    def get_live_rates(self, currencies=None, source=None):
        """
        Real-time exchange rates.

        :param currencies: Specify a comma-separated list of currency codes to limit your API response to
        specific currencies.
        :param source: Specify a source currency.
        :return: JSON or None
        """
        endpoint = 'live'
        params = {
            'source': source,
            'currencies': currencies,
        }
        response = self._make_request(endpoint, params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Request error. Status code: {response.status_code}')
            return None


api = CurrencyAPI(API_KEY)

# print(api.get_change(start_date='2023-09-25', end_date='2023-09-30'))
print(api.get_live_rates(source='RUB', currencies='ARS'))
# print(api.get_list())


