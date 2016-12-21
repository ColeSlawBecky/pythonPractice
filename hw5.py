# hw5.py due 10/19/2016
# Becky Jacob

#Problem 1
#Problem 1a
def getPrices():
    'Create a dictionary prices and populate it with the item name as key and price as value'
    prices = {}
    prices['nails'] = 13.99
    prices['screws'] = 10.99
    prices['anchors'] = 5.29
    prices['twine'] = 2.79
    return prices
'''
>>> p = getPrices()
>>> p
{'nails': 13.99, 'twine': 2.79, 'anchors': 5.29, 'screws': 10.99}
'''

#Problem 1b
def getInventory():
    'create a dictionary inventory and populate with item name as key and number of items as value'
    inventory = {'nails':21,
                 'screws':32,
                 'anchors':0,
                 'twine':7}
    return inventory

'''
>>> i = getInventory()
>>> i
{'anchors': 0, 'nails': 21, 'twine': 7, 'screws': 32}
'''

#Problem 1c
def showPricesAndInventory(prc, inv):
    'will print all prices and inventory'
    for key in inv.keys():
        price = prc[key]
        invNum = inv[key]
        print('{0}: {1} items @ ${2}'.format(key,invNum,price))
        
'''
>>> p = getPrices()
>>> i = getInventory()
>>> showPricesAndInventory(p,i)
screws: 32 items @ $10.99
anchors: 0 items @ $5.29
twine: 7 items @ $2.79
nails: 21 items @ $13.99
'''

#Problem 1d
def calculateReceipt(prc,inv,hardware):
    'will accumulate total price of items in list with inventory greater than 0, will reduce items inventory by the amount purchased, will print the receipt'
    total = 0
    for item in hardware:
        if inv[item] > 0:
            total = total + prc[item]
            inv[item] = inv[item] - 1
    print ('Receipt amount is ${0:.2f}'.format(total))
        
'''
>>> p = getPrices()
>>> i = getInventory()
>>> h1 = ['screws', 'anchors', 'twine']
>>> calculateReceipt(p,i,h1)
Receipt amount is $13.78
>>> h2 = ['twine', 'nails', 'screws']
>>> calculateReceipt(p,i,h2)
Receipt amount is $27.77
>>> i
{'twine': 5, 'anchors': 0, 'nails': 20, 'screws': 30} #I included this to show they were removed from inventory
'''

#Problem 2
#Problem 2a
def read_ticker(filename):
    'read file, store the ticker and name of each company in a dictionary and return the resulting dictionary'
    tickers = {}
    infile = open(filename, 'r')
    for line in infile:
        newLine = line.strip()
        split = newLine.split(',')
        tick = split[0]
        name = split[1]
        tickers[tick] = name
    infile.close()
    return tickers

'''
>>> tickers = read_ticker( 'tickers.csv')
>>> tickers[ 'BJRI' ]
"BJ's Restaurants Inc."
'''

#Problem 2b
def ticker(filename):
    'run read_ticker(), assign dictionary to a variable, if user hits Enter the loop exits, if user enters ticker, the company name is printed, or a warning if ticker does not exist'
    tickers = read_ticker(filename)
    while True:
        ticker = input('Please enter a ticker symbol: ')
        if ticker == '':
            break
        elif ticker not in tickers:
            print('Ticker symbol "{0}" not found.'.format(ticker))
        elif ticker in tickers:
            print('Company "{0}" has ticker symbol {1}.'.format(tickers[ticker],ticker))
        
'''
>>> ticker( 'tickers.csv' )
Please enter a ticker symbol: YHOO
Company "Yahoo! Inc." has ticker symbol YHOO.
Please enter a ticker symbol: DKS
Company "Dick's Sporting Goods Inc." has ticker symbol DKS.
Please enter a ticker symbol: GOOGLE
Ticker symbol "GOOGLE" not found.
Please enter a ticker symbol: 
>>> 
'''      


