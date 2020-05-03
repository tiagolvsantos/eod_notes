#https://github.com/man-group/dtale
#pip install dtale
#pip install yfinance

import dtale
import yfinance as yf


def getSymbolHistoricalPrice(tickerSymbol):
    try:
        ticker = yf.Ticker(tickerSymbol)
        tickerHistPrice = ticker.history("max")
        return tickerHistPrice
    except NameError:
        return NameError
    

ticker="SPY"
dfQuoteData= getSymbolHistoricalPrice(ticker)
d= dtale.show(dfQuoteData)
d.open_browser()