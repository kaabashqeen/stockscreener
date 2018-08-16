import request, time

stockToPull = 'AAPL'

def pullData(stock):
    try:
        stockFile = stock + '.txt'
        urlToVisit = 'https://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=1y/csv'
        stockData = urllib.o
    except Exception as e:
        print('main loop', str(e))