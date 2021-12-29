# coinbase bot by Daniel Saisani
import coinbase
from coinbase.wallet.client import Client
from coinbaseKeys import coinbase_API_key, coinbase_API_secret
from coinbase.wallet.error import AuthenticationError
print("Hello Coinbase World!")
try:
    client = Client(coinbase_API_key,coinbase_API_secret)
except:
    print("There was an issue initialising coinbase wallet!")
myWallet = client.get_accounts()
# print(myWallet.balance)