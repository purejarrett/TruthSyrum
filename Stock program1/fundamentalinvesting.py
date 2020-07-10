import time
import urllib2
from urllib2 import urlopen

sp500short = ['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'adbe', 'adm', 'adp']

my_stocks = ['f', 'aple', 'bcrx']

def yahookeystats(stock):
    try:
        sourcecode = urllib2.urlopen()
        
    except Exception,e:
        print 'failed in the main loop',str(e'