import requests
from bs4 import BeautifulSoup
import redis
import pymongo
from pymongo import MongoClient


connectionRedis = redis.Redis(host = '127.0.0.1', port = 6379)
connectionMongo = MongoClient("mongodb://127.0.0.1:27017")
database = connectionMongo["DBA"]
collection = database["Transactions"]

def scraper(transaction):
    r = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions")
    soup = BeautifulSoup(r.text, "html.parser")
    lines = soup.find_all('div', {"class", "sc-6nt7oh-0 PtIAf"})

    i = 0
    h = 0
    time = 1
    btc = 2
    usd = 3
    if transaction == None:
        lastTime = 0
    else:
        lastTime = transaction['time']

    while i < (len(lines)/4):
        if i == 0:
            if transaction == None: # If this is the first time running the script create the dictionary to make storing the transactions easier
                transaction = {'h': lines[h].getText(), 'time': lines[time].getText(), 'btc': lines[btc].getText(), 'usd': lines[usd].getText()}
            i += 1
            h += 4
            time += 4
            btc += 4
            usd += 4
            lastTime = transaction['time'] 
            
        else:
            if lastTime != lines[time].getText(): # This is where the time changes, which means whatever value we're holding right now for that set minute is the transaction with the highest value there is
                #print('\n', "This is it the highest: \n", transaction) we no longer need to print it to the console since we have a database now
                collection.insert_one(transaction) # Entering our transaction with the highest value of the minute to our mongoDB
                lastTime = lines[time].getText()
                transaction = {'h': lines[h].getText(), 'time': lines[time].getText(), 'btc': lines[btc].getText(), 'usd': lines[usd].getText()}
                i += 1
                h += 4
                time += 4
                btc += 4
                usd += 4            
            else:                
                if transaction['btc'].split(' ')[0] < lines[btc].getText().split(' ')[0]: #comparing the last scraped transaction with the next one and keeping only the highest one
                    transaction = {'h': lines[h].getText(), 'time': lines[time].getText(), 'btc': lines[btc].getText(), 'usd': lines[usd].getText()}
                    i += 1
                    h += 4
                    time += 4
                    btc += 4
                    usd += 4
                else:
                    i += 1
                    h += 4
                    time += 4
                    btc += 4
                    usd += 4                
    #scraper(url, transaction)
    return transaction


url = "https://www.blockchain.com/btc/unconfirmed-transactions"
transaction = None
while True:
    lastTransaction = scraper(transaction)
    transaction = scraper(lastTransaction)
print()


