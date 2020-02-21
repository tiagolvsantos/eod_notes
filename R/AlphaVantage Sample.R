library(alphavantager)
library(xlsx)

av_api_key("YOUR_API_KEY")

#Daily data
quoteData <- av_get(
  symbol = "AAPL",
  av_fun = "TIME_SERIES_DAILY",
  outputsize = "full"
)


#Hourly data
quoteData <- av_get(
  symbol = "AAPL",
  av_fun = "TIME_SERIES_INTRADAY",
  interval = "60min",
  outputsize = "full"
)


write.xlsx(quoteData, "C:\\Folder\\AAPL.xlsx",sheetName = "Daily data")