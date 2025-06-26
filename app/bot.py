from binance import Client

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        self.client = None  # Don't connect yet

    def _connect(self):
        if self.client is None:
            self.client = Client(self.api_key, self.api_secret)
            if self.testnet:
                self.client.FUTURES_URL = self.client.FUTURES_TESTNET_URL

    def get_balance(self):
        self._connect()
        return self.client.futures_account_balance()

    def create_order(self, **args):
        self._connect()
        return self.client.futures_create_order(**args)

    def get_position_info(self):
        self._connect()
        return self.client.futures_position_information()

    def cancel_order(self, **args):
        self._connect()
        return self.client.futures_cancel_order(**args)
