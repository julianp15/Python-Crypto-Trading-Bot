import cbpro
import time

public_client = cbpro.PublicClient()

#Coinbase Pro Data Querying functions
def get_Options():
    #Get crypto purchasing options from Coinbase Pro
    result = public_client.get_products()

    #Print results of data queried from Coinbase
    for row in result:
        print(row['id'])

def get_cbTime():
    #Gets time from exchange and prints it
    cbTime = public_client.get_time()
    print(cbTime)

def get_Price():
    #Gets ETH ticker information
    cbPrice = auth_client.get_product_ticker('ETH-USDC')
    print(cbPrice)

def get_Stats():
    #Gets ETH 24 hour performance stats
    cbStats = public_client.get_product_24hr_stats('ETH-USDC')
    print(cbStats)

#Coinbase PRO Trading functions

#Gets API permission keys and establishes connection to connected CBPro account
data = open('passphrase.txt', 'r').read().splitlines()
public = data[0]
passphrase = data[1]
secret = data[2]

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)
#print(auth_client.get_accounts())

#Execute buys
##def buy_Limit():
    #Limit order ETH purchase
  ##  print(auth_client.buy(price="10.0", size="0.1", order_type="limit", product_id ="ETH-USDC"))

def buy_Market():
    #Market order ETH purchase
    print(auth_client.buy(size="0.00090322", order_type="market", product_id="ETH-USDC"))

#Execute sells
def sell_Market():
    #Market order ETH sell
    print(auth_client.sell(size="0.00090322", order_type="market", product_id="ETH-USDC"))


def panicButton():
    #Cancels all orders
    print(auth_client.cancel_all(product_id="ETH-USDC"))


#Automated trading functions

#If ETH hits sell price, sell
sell_price = 3305
sell_amount = 0.00090322 

#If ETH hits buy price, buy
buy_price = 3302
buy_amount = 0.00090322

#Run bot
while True:
    price = float(auth_client.get_product_ticker(product_id="ETH-USDC")['price'])
    if price <= buy_price:
        print("Buying ETH")
        buy_Market()
    elif price >= sell_price:
        print("Selling ETH")
        sell_Market()
    else:
        print("Nothing....")
    time.sleep(10)