library(quantmod)
library(ggplot2)
library(hrbrthemes)
library(plotly)


#sET TIME PERIOD
days= 90

# DEFINE TICKER
ticker = "AAPL"

# RETRIEVE DATA
quoteData = tail(as.data.frame(na.omit(getSymbols.yahoo(ticker, periodicity = "daily", auto.assign=FALSE))),n=days)
# CONVERT INDEX TO DATE
quoteData <- cbind(date=as.Date(rownames(quoteData)),quoteData)
# RENAME COLUMNS
colnames(quoteData) = c("date","open","high","low","close","volume","adj.")

# CALCULATE MEANS AND STANDARD DEVIATIONS
for (i in 1:nrow(quoteData))
{
  quoteData[i,"geoMean"]= rbind(exp(mean(log(quoteData[i:1,"close"]))))
  quoteData[i,"Mean"]= rbind(mean(quoteData[i:1,"close"]))
  quoteData[i,"stDev"]= rbind(StdDev(quoteData[i:1,"close"]))
}

# PLOT THE CHART
# YOU CAN USE THE VANILLA GGPLOT ALTHOUGH I RECOMEND USING THE PLOTLY ADDON. IT WILL ALLOW YOU TO NAVIGATE TRHOUGH THE CHART.

p<-ggplot() + 
geom_line( data =quoteData,aes(x = date,y = close ,color = "Close"),size=1,group = 1) + 
geom_line( data =quoteData,aes(x = date,y = geoMean ,color = "geoMean"),size=1,group = 1) + 
geom_line( data =quoteData,aes(x = date,y = Mean ,color = "Mean"),size=1,group = 1) + 
geom_line( data =quoteData,aes(x = date,y = (tail(quoteData[,"close"],n=1)-tail(quoteData[,"stDev"],n=1)) ,color = "SD-1"),size=1,group = 1) + 
geom_line( data =quoteData,aes(x = date,y = (tail(quoteData[,"close"],n=1)+tail(quoteData[,"stDev"],n=1)) ,color = "SD+1"),size=1,group = 1) + 
geom_smooth(model="lm", color = "white")+ 
labs(title = paste0(gsub('_','/',ticker)," Last ",days," days"), subtitle = paste0("Last: " ,round(tail(quoteData[,"close"],n=1),digits = 4),
                                                                                  " | SD-1: ",round((tail(quoteData[,"close"],n=1)-tail(quoteData[,"stDev"],n=1)),digits = 4),
                                                                                  " | SD+1: ",round((tail(quoteData[,"close"],n=1)+tail(quoteData[,"stDev"],n=1)),digits = 4),
                                                                                  " | Mean: " ,round(tail(quoteData$Mean,n=1),digits = 4),
                                                                                  " | GeoMean: " ,round(tail(quoteData$geoMean,n=1),digits = 4)), caption = "@tiagolvsantos") +  
scale_x_date(limits = as.Date(c(Sys.Date()-days,Sys.Date())))+
scale_color_manual(name = "", 
                  values = c("Close" = "white", "geoMean" = "yellow","Mean"="#FF6E4A","SD-1"="purple","SD+1"="pink")) +theme_modern_rc() 

ggplotly(p)


