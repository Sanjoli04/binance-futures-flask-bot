from binance import Client

class BasicBot:
    def __init__(self, api_key, api_secret, testnet = True):
        if testnet:
            self.client = Client(api_key, api_secret, base_url='https://testnet.binancefuture.com')
        else:
            self.client = Client(api_key, api_secret)
    def get_balance(self):
        return self.client.futures_account_balance()
    def create_order(self,**args):
        return self.client.futures_create_order(**args)
    def get_position_info(self):
        return self.client.futures_position_information()
    def cancel_order(self,**args):
        return self.client.futures_cancel_order(**args)