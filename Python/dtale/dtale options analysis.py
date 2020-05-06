#https://github.com/man-group/dtale
#pip install dtale
#pip install yfinance

import dtale
import yfinance as yf
import pandas as pd

symbol="SPY"
period= 1
# GET SYMBOL CALLS
def getOptionCalls(symbol,period):
    try:
        ticker = yf.Ticker(symbol)
        #Expiration periods ex: 1 is the first expiration period
        optionChain = ticker.option_chain(ticker.options[period])
        optionCalls = optionChain[0]
        return optionCalls
    except NameError:
        return NameError    

# GET SYMBOL PUTS
def getOptionPuts(symbol,period):
    try:
        ticker = yf.Ticker(symbol)
        #Expiration periods ex: 1 is the first expiration period
        optionChain = ticker.option_chain(ticker.options[period])
        optionPuts= optionChain[1]
        return optionPuts
    except NameError:
        return NameError   


options=getOptionPuts(symbol,period)
d= dtale.show(options)
d.open_browser()
