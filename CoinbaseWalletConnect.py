# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:47:41 2021

@author: macke
"""
from coinbase.wallet.client import Client
from time import sleep
from data import percentage_change, api_key, api_secret

#https://developers.coinbase.com/docs/wallet/guides/buy-sell
api_key = api_key()
api_secret = api_secret()
#Setting up coinbase client
client = Client(api_key, api_secret)
#payment_method = client.get_payment_methods()[0] //USED TO GRAB PAYMENT ID TO ACTUALLY MAKE THE PURCHASE

#Take user input
user_limit_order = float(input("Enter a price for your Bitcoin limit order (USD): "))
user_amount_spent = float(input("Enter how much you want to spend (USD): "))

#Creating the loop
currency_code = 'USD'

start_price = client.get_spot_price(currency=currency_code)


while(True):

    #Reset currents and find percentage change
    buy_price = client.get_buy_price(currency=currency_code)
    percentage_gainloss = (percentage_change(start_price.amount, buy_price.amount))


    #print bitcoin curent price, and percentage chage
    print('Bitcoin is ' + str(buy_price.amount) + '\nPercent change in last 60 seconds: ' + percentage_gainloss+ '%')

    #Within Purchase Threshold
    if(float(buy_price.amount) <= user_limit_order):

 #      buy = client.buy(amount=str(user_amount_spent / float(buy_price.amount), currency=currency_code, payment_method=payment_method.id))

        print("Bought $" + str(user_amount_spent) + " or " + str(user_amount_spent / float(buy_price.amount)) + " bitcoin at " + buy_price.amount)

    sleep(60)

    #Update start_price
    start_price = buy_price

#%%

total = 0
message = [ ]
accounts = client.get_accounts()
for wallet in accounts.data:
    message.append( str(wallet['name']) + ' ' +   str(wallet['native_balance']) )
    value = str( wallet['native_balance']).replace('USD','')
    total += float(value)
message.append( 'Total Balance: ' + 'USD ' + str(total) )
print ('\n'.join( message ))
#%%

