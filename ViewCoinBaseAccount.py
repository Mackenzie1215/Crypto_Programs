import csv
import time
import pandas as pd
import datetime
import csv
import time
from coinbase.wallet.client import Client
from datetime import datetime

coinbase_API_key = 'Your key'
coinbase_API_secret = 'your api'
client = Client(coinbase_API_key, coinbase_API_secret)

def Get_Price(Code):
    currency_code = Code
    buy_price = client.get_buy_price(currency_pair= currency_code)
    return(buy_price['amount'])

def Check_Account():
    total = 0
    message = [ ]
    
    accounts = client.get_accounts()
    for wallet in accounts.data:
        message.append( str(wallet['name']) + ' ' +   str(wallet['native_balance']) )
        value = str( wallet['native_balance']).replace('USD','')
        total += float(value)
    message.append( 'Total Balance: ' + 'USD ' + str(total) )
    print ('\n'.join( message ))
    
    
def Get_Da_price_Tho():
    counter_df = pd.read_csv('CryptoLocalData\LTC_File.csv')
    index = counter_df.index
    
    # get the count of rows currently in my file
    count = len(index)
    
    # Set x to the current number of rows in my file
    x = count
    
    ## Open our file in ppend mode to add to whats already there
    file1 = open("CryptoLocalData\LTC_File.csv", "a")  # append mode
    
    # Runs my Find_Price function to get the price at that specific runtime
    LTC = Get_Price('LTC-USD')
    
    # Gets  the current datetime to log with the price
    now = datetime.now()
    date = now.strftime("%m/%d/%Y %H:%M:%S")

    # Writes the price and the current datetime to the LTC_File
    fieldnames = ['Price', 'Time', 'Count']
    writer = csv.DictWriter(file1, fieldnames=fieldnames)
    writer.writerow({'Price': LTC, 'Time': date, 'Count' : x})
    
    # If the Current count is a multiple of 5 we print it to 
    # see whats going on in realtime
    if(x % 5 == 0):
            print(x, ',',LTC, ',', date)
            file2 = open("CryptoLocalData\LTC_File_LowDetail.csv", "a")
            writer2 = csv.DictWriter(file2, fieldnames=fieldnames)
            writer2.writerow({'Price': LTC, 'Time': date, 'Count' : x})
            
            file2.close()
    # Close the file to save what was entered
    file1.close()
    
    # Let the program sleep for 1 minute to give the 
    # price a chance to change
    time.sleep(60)  
