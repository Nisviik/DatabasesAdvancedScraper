#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup

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
            if transaction == None:
                transaction = {'h': lines[h].getText(), 'time': lines[time].getText(), 'btc': lines[btc].getText(), 'usd': lines[usd].getText()}
            i += 1
            h += 4
            time += 4
            btc += 4
            usd += 4
            lastTime = transaction['time'] 
            
        else:
            if lastTime != lines[time].getText():
                print('\n', "This is it the highest: \n", transaction)
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


