import quandl
from datetime import datetime, timedelta
import pandas as pd

#Quandl API
quandl.ApiConfig.api_key = "YOUR_API_KEY"

#Define dates - > Date from the last CoT Report ( today date minus x days)
#you can find all the information about the CoT reports here https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm´

date = datetime.today() - timedelta(days=15)


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('COT Report weekly extraction.xlsx', engine='xlsxwriter')

#Create Dataframe Commodities
COT_Commodities = pd.DataFrame(columns = [
     "Date",   
    "Ticker",
    "Open Interest",
    "Producer/Merchant/Processor/User Longs",
    "Producer/Merchant/Processor/User Shorts",
    "Swap Dealer Longs",
    "Swap Dealer Shorts",
    "Swap Dealer Spreads",
    "Money Manager Longs",
    "Money Manager Shorts",
    "Money Manager Spreads",
    "Other Reportable Longs",
    "Other Reportable Shorts",
    "Other Reportable Spreads",
    "Total Reportable Longs",
    "Total Reportable Shorts",
    "Non Reportable Longs",
    "Non Reportable Shorts"
])

#Commitment of Traders - WTI MIDLAND ARGUS VS WTI TRADE (NYME) - Futures and Options (067A71)
cotWTI =quandl.get('CFTC/067A71_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {   "Date":date,
            "Ticker":"WTI",
            "Open Interest":cotWTI.iloc[0]['Open Interest'],
            "Producer/Merchant/Processor/User Longs": cotWTI.iloc[0]['Producer/Merchant/Processor/User Longs'],
            "Producer/Merchant/Processor/User Shorts": cotWTI.iloc[0]['Producer/Merchant/Processor/User Shorts'],
            "Swap Dealer Longs": cotWTI.iloc[0]['Swap Dealer Longs'],
            "Swap Dealer Shorts": cotWTI.iloc[0]['Swap Dealer Shorts'],
            "Swap Dealer Spreads": cotWTI.iloc[0]['Swap Dealer Spreads'],
            "Money Manager Longs" : cotWTI.iloc[0]['Money Manager Longs'],
            "Money Manager Shorts": cotWTI.iloc[0]['Money Manager Shorts'],
            "Money Manager Spreads": cotWTI.iloc[0]['Money Manager Spreads'],
            "Other Reportable Longs" : cotWTI.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotWTI.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotWTI.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotWTI.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotWTI.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotWTI.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotWTI.iloc[0]['Non Reportable Shorts']
               
        }, index=[0])
COT_Commodities=COT_Commodities.append(newRow)[COT_Commodities.columns.tolist()]

#Commitment of Traders - GASOLINE BLENDSTOCK (RBOB) (NYME) - Futures and Options (111659)
cotRBOB =quandl.get('CFTC/111659_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {   "Date":date,
            "Ticker":"RBOB",
            "Open Interest":cotRBOB.iloc[0]['Open Interest'],
            "Producer/Merchant/Processor/User Longs": cotRBOB.iloc[0]['Producer/Merchant/Processor/User Longs'],
            "Producer/Merchant/Processor/User Shorts": cotRBOB.iloc[0]['Producer/Merchant/Processor/User Shorts'],
            "Swap Dealer Longs": cotRBOB.iloc[0]['Swap Dealer Longs'],
            "Swap Dealer Shorts": cotRBOB.iloc[0]['Swap Dealer Shorts'],
            "Swap Dealer Spreads": cotRBOB.iloc[0]['Swap Dealer Spreads'],
            "Money Manager Longs" : cotRBOB.iloc[0]['Money Manager Longs'],
            "Money Manager Shorts": cotRBOB.iloc[0]['Money Manager Shorts'],
            "Money Manager Spreads": cotRBOB.iloc[0]['Money Manager Spreads'],
            "Other Reportable Longs" : cotRBOB.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotRBOB.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotRBOB.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotRBOB.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotRBOB.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotRBOB.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotRBOB.iloc[0]['Non Reportable Shorts']
               
        }, index=[1])
COT_Commodities=COT_Commodities.append(newRow)[COT_Commodities.columns.tolist()]

#Commitment of Traders - NATURAL GAS (NYME) - Futures and Options (023651)
cotNATGAS =quandl.get('CFTC/023651_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {   "Date":date,
            "Ticker":"NATGAS",
            "Open Interest":cotNATGAS.iloc[0]['Open Interest'],
            "Producer/Merchant/Processor/User Longs": cotNATGAS.iloc[0]['Producer/Merchant/Processor/User Longs'],
            "Producer/Merchant/Processor/User Shorts": cotNATGAS.iloc[0]['Producer/Merchant/Processor/User Shorts'],
            "Swap Dealer Longs": cotNATGAS.iloc[0]['Swap Dealer Longs'],
            "Swap Dealer Shorts": cotNATGAS.iloc[0]['Swap Dealer Shorts'],
            "Swap Dealer Spreads": cotNATGAS.iloc[0]['Swap Dealer Spreads'],
            "Money Manager Longs" : cotNATGAS.iloc[0]['Money Manager Longs'],
            "Money Manager Shorts": cotNATGAS.iloc[0]['Money Manager Shorts'],
            "Money Manager Spreads": cotNATGAS.iloc[0]['Money Manager Spreads'],
            "Other Reportable Longs" : cotNATGAS.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotNATGAS.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotNATGAS.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotNATGAS.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotNATGAS.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotNATGAS.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotNATGAS.iloc[0]['Non Reportable Shorts']
               
        }, index=[2])
COT_Commodities=COT_Commodities.append(newRow)[COT_Commodities.columns.tolist()]

#Commitment of Traders - SILVER (CMX) - Futures and Options (084691)
cotXAG =quandl.get('CFTC/084691_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {   "Date":date,
            "Ticker":"XAG",
            "Open Interest":cotXAG.iloc[0]['Open Interest'],
            "Producer/Merchant/Processor/User Longs": cotXAG.iloc[0]['Producer/Merchant/Processor/User Longs'],
            "Producer/Merchant/Processor/User Shorts": cotXAG.iloc[0]['Producer/Merchant/Processor/User Shorts'],
            "Swap Dealer Longs": cotXAG.iloc[0]['Swap Dealer Longs'],
            "Swap Dealer Shorts": cotXAG.iloc[0]['Swap Dealer Shorts'],
            "Swap Dealer Spreads": cotXAG.iloc[0]['Swap Dealer Spreads'],
            "Money Manager Longs" : cotXAG.iloc[0]['Money Manager Longs'],
            "Money Manager Shorts": cotXAG.iloc[0]['Money Manager Shorts'],
            "Money Manager Spreads": cotXAG.iloc[0]['Money Manager Spreads'],
            "Other Reportable Longs" : cotXAG.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotXAG.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotXAG.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotXAG.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotXAG.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotXAG.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotXAG.iloc[0]['Non Reportable Shorts']
               
        }, index=[3])
COT_Commodities=COT_Commodities.append(newRow)[COT_Commodities.columns.tolist()]

#Commitment of Traders - GOLD (CMX) - Futures and Options (088691)
cotXAU =quandl.get('CFTC/088691_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {   "Date":date,
            "Ticker":"XAU",
            "Open Interest":cotXAU.iloc[0]['Open Interest'],
            "Producer/Merchant/Processor/User Longs": cotXAU.iloc[0]['Producer/Merchant/Processor/User Longs'],
            "Producer/Merchant/Processor/User Shorts": cotXAU.iloc[0]['Producer/Merchant/Processor/User Shorts'],
            "Swap Dealer Longs": cotXAU.iloc[0]['Swap Dealer Longs'],
            "Swap Dealer Shorts": cotXAU.iloc[0]['Swap Dealer Shorts'],
            "Swap Dealer Spreads": cotXAU.iloc[0]['Swap Dealer Spreads'],
            "Money Manager Longs" : cotXAU.iloc[0]['Money Manager Longs'],
            "Money Manager Shorts": cotXAU.iloc[0]['Money Manager Shorts'],
            "Money Manager Spreads": cotXAU.iloc[0]['Money Manager Spreads'],
            "Other Reportable Longs" : cotXAU.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotXAU.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotXAU.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotXAU.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotXAU.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotXAU.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotXAU.iloc[0]['Non Reportable Shorts']
               
        }, index=[4])
COT_Commodities=COT_Commodities.append(newRow)[COT_Commodities.columns.tolist()]

#Commitment of Traders - SUGAR NO. 11 (ICUS) - Futures and Options (080732)
cotSUGAR =quandl.get('CFTC/080732_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {   "Date":date,
            "Ticker":"SUGAR",
            "Open Interest":cotSUGAR.iloc[0]['Open Interest'],
            "Producer/Merchant/Processor/User Longs": cotSUGAR.iloc[0]['Producer/Merchant/Processor/User Longs'],
            "Producer/Merchant/Processor/User Shorts": cotSUGAR.iloc[0]['Producer/Merchant/Processor/User Shorts'],
            "Swap Dealer Longs": cotSUGAR.iloc[0]['Swap Dealer Longs'],
            "Swap Dealer Shorts": cotSUGAR.iloc[0]['Swap Dealer Shorts'],
            "Swap Dealer Spreads": cotSUGAR.iloc[0]['Swap Dealer Spreads'],
            "Money Manager Longs" : cotSUGAR.iloc[0]['Money Manager Longs'],
            "Money Manager Shorts": cotSUGAR.iloc[0]['Money Manager Shorts'],
            "Money Manager Spreads": cotSUGAR.iloc[0]['Money Manager Spreads'],
            "Other Reportable Longs" : cotSUGAR.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotSUGAR.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotSUGAR.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotSUGAR.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotSUGAR.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotSUGAR.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotSUGAR.iloc[0]['Non Reportable Shorts']
               
        }, index=[5])
COT_Commodities=COT_Commodities.append(newRow)[COT_Commodities.columns.tolist()]

#Commitment of Traders - WHEAT-HRW (CBT) - Futures and Options (001612)
cotWHEAT =quandl.get('CFTC/001612_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {   "Date":date,
            "Ticker":"WHEAT",
            "Open Interest":cotWHEAT.iloc[0]['Open Interest'],
            "Producer/Merchant/Processor/User Longs": cotWHEAT.iloc[0]['Producer/Merchant/Processor/User Longs'],
            "Producer/Merchant/Processor/User Shorts": cotWHEAT.iloc[0]['Producer/Merchant/Processor/User Shorts'],
            "Swap Dealer Longs": cotWHEAT.iloc[0]['Swap Dealer Longs'],
            "Swap Dealer Shorts": cotWHEAT.iloc[0]['Swap Dealer Shorts'],
            "Swap Dealer Spreads": cotWHEAT.iloc[0]['Swap Dealer Spreads'],
            "Money Manager Longs" : cotWHEAT.iloc[0]['Money Manager Longs'],
            "Money Manager Shorts": cotWHEAT.iloc[0]['Money Manager Shorts'],
            "Money Manager Spreads": cotWHEAT.iloc[0]['Money Manager Spreads'],
            "Other Reportable Longs" : cotWHEAT.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotWHEAT.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotWHEAT.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotWHEAT.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotWHEAT.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotWHEAT.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotWHEAT.iloc[0]['Non Reportable Shorts']
               
        }, index=[6])
COT_Commodities=COT_Commodities.append(newRow)[COT_Commodities.columns.tolist()]

#Commitment of Traders - CORN (CBT) - Futures and Options (002602)
cotCORN =quandl.get('CFTC/002602_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {   "Date":date,
            "Ticker":"CORN",
            "Open Interest":cotCORN.iloc[0]['Open Interest'],
            "Producer/Merchant/Processor/User Longs": cotCORN.iloc[0]['Producer/Merchant/Processor/User Longs'],
            "Producer/Merchant/Processor/User Shorts": cotCORN.iloc[0]['Producer/Merchant/Processor/User Shorts'],
            "Swap Dealer Longs": cotCORN.iloc[0]['Swap Dealer Longs'],
            "Swap Dealer Shorts": cotCORN.iloc[0]['Swap Dealer Shorts'],
            "Swap Dealer Spreads": cotCORN.iloc[0]['Swap Dealer Spreads'],
            "Money Manager Longs" : cotCORN.iloc[0]['Money Manager Longs'],
            "Money Manager Shorts": cotCORN.iloc[0]['Money Manager Shorts'],
            "Money Manager Spreads": cotCORN.iloc[0]['Money Manager Spreads'],
            "Other Reportable Longs" : cotCORN.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotCORN.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotCORN.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotCORN.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotCORN.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotCORN.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotCORN.iloc[0]['Non Reportable Shorts']
               
        }, index=[7])
COT_Commodities=COT_Commodities.append(newRow)[COT_Commodities.columns.tolist()]

#Commitment of Traders - SOYBEANS (CBT) - Futures and Options (005602)
cotSOYBEANS =quandl.get('CFTC/005602_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {   "Date":date,
            "Ticker":"SOYBEANS",
            "Open Interest":cotSOYBEANS.iloc[0]['Open Interest'],
            "Producer/Merchant/Processor/User Longs": cotSOYBEANS.iloc[0]['Producer/Merchant/Processor/User Longs'],
            "Producer/Merchant/Processor/User Shorts": cotSOYBEANS.iloc[0]['Producer/Merchant/Processor/User Shorts'],
            "Swap Dealer Longs": cotSOYBEANS.iloc[0]['Swap Dealer Longs'],
            "Swap Dealer Shorts": cotSOYBEANS.iloc[0]['Swap Dealer Shorts'],
            "Swap Dealer Spreads": cotSOYBEANS.iloc[0]['Swap Dealer Spreads'],
            "Money Manager Longs" : cotSOYBEANS.iloc[0]['Money Manager Longs'],
            "Money Manager Shorts": cotSOYBEANS.iloc[0]['Money Manager Shorts'],
            "Money Manager Spreads": cotSOYBEANS.iloc[0]['Money Manager Spreads'],
            "Other Reportable Longs" : cotSOYBEANS.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotSOYBEANS.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotSOYBEANS.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotSOYBEANS.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotSOYBEANS.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotSOYBEANS.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotSOYBEANS.iloc[0]['Non Reportable Shorts']
               
        }, index=[8])
COT_Commodities=COT_Commodities.append(newRow)[COT_Commodities.columns.tolist()]

# Convert the dataframe to an XlsxWriter Excel object.
COT_Commodities.to_excel(writer, sheet_name='Commodities')



#Create Dataframe Stocks & Indexes
COT_Stocks_Indexes = pd.DataFrame(columns = [
     "Date",   
    "Ticker",
    "Open Interest",
    "Dearler Longs",
    "Dealer Shorts",
    "Dealer Spreads",
    "Asset Manager Longs",
    "Asset Manager Shorts",
    "Asset Manager Spreads",
    "Leveraged Funds Longs",
    "Leveraged Funds Shorts",
    "Leveraged Funds Spreads",
    "Other Reportable Longs",
    "Other Reportable Shorts",
    "Other Reportable Spreads",
    "Total Reportable Longs",
    "Total Reportable Shorts",
    "Non Reportable Longs",
    "Non Reportable Shorts"
])


#Commitment of Traders - S&P 500 Consolidated (CME) - Futures and Options (13874P)
cotSP500 =quandl.get('CFTC/13874P_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {    "Date":date,   
            "Ticker":"S&P500",
            "Open Interest":cotSP500.iloc[0]['Open Interest'],
            "Dealer Longs":cotSP500.iloc[0]['Dealer Longs'],
            "Dealer Shorts":cotSP500.iloc[0]['Dealer Shorts'],
            "Dealer Spreads":cotSP500.iloc[0]['Dealer Spreads'],
            "Asset Manager Longs":cotSP500.iloc[0]['Asset Manager Longs'],
            "Asset Manager Shorts":cotSP500.iloc[0]['Asset Manager Shorts'],
            "Asset Manager Spreads":cotSP500.iloc[0]['Asset Manager Spreads'],
            "Leveraged Funds Longs":cotSP500.iloc[0]['Leveraged Funds Longs'],
            "Leveraged Funds Shorts":cotSP500.iloc[0]['Leveraged Funds Shorts'],
            "Leveraged Funds Spreads":cotSP500.iloc[0]['Leveraged Funds Spreads'],
            "Other Reportable Longs":cotSP500.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotSP500.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotSP500.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotSP500.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotSP500.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotSP500.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotSP500.iloc[0]['Non Reportable Shorts']
               
        }, index=[0])
COT_Stocks_Indexes=COT_Stocks_Indexes.append(newRow)[COT_Stocks_Indexes.columns.tolist()]

#Commitment of Traders - NASDAQ-100 Consolidated (CME) - Futures and Options (20974P)
cotNDQ100 =quandl.get('CFTC/20974P_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {    "Date":date,   
            "Ticker":"NASDAQ100",
            "Open Interest":cotNDQ100.iloc[0]['Open Interest'],
            "Dealer Longs":cotNDQ100.iloc[0]['Dealer Longs'],
            "Dealer Shorts":cotNDQ100.iloc[0]['Dealer Shorts'],
            "Dealer Spreads":cotNDQ100.iloc[0]['Dealer Spreads'],
            "Asset Manager Longs":cotNDQ100.iloc[0]['Asset Manager Longs'],
            "Asset Manager Shorts":cotNDQ100.iloc[0]['Asset Manager Shorts'],
            "Asset Manager Spreads":cotNDQ100.iloc[0]['Asset Manager Spreads'],
            "Leveraged Funds Longs":cotNDQ100.iloc[0]['Leveraged Funds Longs'],
            "Leveraged Funds Shorts":cotNDQ100.iloc[0]['Leveraged Funds Shorts'],
            "Leveraged Funds Spreads":cotNDQ100.iloc[0]['Leveraged Funds Spreads'],
            "Other Reportable Longs":cotNDQ100.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotNDQ100.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotNDQ100.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotNDQ100.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotNDQ100.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotNDQ100.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotNDQ100.iloc[0]['Non Reportable Shorts']
               
        }, index=[1])
COT_Stocks_Indexes=COT_Stocks_Indexes.append(newRow)[COT_Stocks_Indexes.columns.tolist()]

#Commitment of Traders - VIX FUTURES (E) - Futures and Options (1170E1)
cotVIX =quandl.get('CFTC/1170E1_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {    "Date":date,   
            "Ticker":"VIX",
            "Open Interest":cotVIX.iloc[0]['Open Interest'],
            "Dealer Longs":cotVIX.iloc[0]['Dealer Longs'],
            "Dealer Shorts":cotVIX.iloc[0]['Dealer Shorts'],
            "Dealer Spreads":cotVIX.iloc[0]['Dealer Spreads'],
            "Asset Manager Longs":cotVIX.iloc[0]['Asset Manager Longs'],
            "Asset Manager Shorts":cotVIX.iloc[0]['Asset Manager Shorts'],
            "Asset Manager Spreads":cotVIX.iloc[0]['Asset Manager Spreads'],
            "Leveraged Funds Longs":cotVIX.iloc[0]['Leveraged Funds Longs'],
            "Leveraged Funds Shorts":cotVIX.iloc[0]['Leveraged Funds Shorts'],
            "Leveraged Funds Spreads":cotVIX.iloc[0]['Leveraged Funds Spreads'],
            "Other Reportable Longs":cotVIX.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotVIX.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotVIX.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotVIX.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotVIX.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotVIX.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotVIX.iloc[0]['Non Reportable Shorts']
               
        }, index=[2])
COT_Stocks_Indexes=COT_Stocks_Indexes.append(newRow)[COT_Stocks_Indexes.columns.tolist()]

# Convert the dataframe to an XlsxWriter Excel object.
COT_Stocks_Indexes.to_excel(writer, sheet_name='Stocks & Indexes')



#Create Dataframe Currencies
COT_Currencies= pd.DataFrame(columns = [
     "Date",   
    "Ticker",
    "Open Interest",
    "Dearler Longs",
    "Dealer Shorts",
    "Dealer Spreads",
    "Asset Manager Longs",
    "Asset Manager Shorts",
    "Asset Manager Spreads",
    "Leveraged Funds Longs",
    "Leveraged Funds Shorts",
    "Leveraged Funds Spreads",
    "Other Reportable Longs",
    "Other Reportable Shorts",
    "Other Reportable Spreads",
    "Total Reportable Longs",
    "Total Reportable Shorts",
    "Non Reportable Longs",
    "Non Reportable Shorts"
])

#Commitment of Traders - EURO FX (CME) - Futures and Options (099741)
cotEURO =quandl.get('CFTC/099741_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {    "Date":date,   
            "Ticker":"EURO",
            "Open Interest":cotEURO.iloc[0]['Open Interest'],
            "Dealer Longs":cotEURO.iloc[0]['Dealer Longs'],
            "Dealer Shorts":cotEURO.iloc[0]['Dealer Shorts'],
            "Dealer Spreads":cotEURO.iloc[0]['Dealer Spreads'],
            "Asset Manager Longs":cotEURO.iloc[0]['Asset Manager Longs'],
            "Asset Manager Shorts":cotEURO.iloc[0]['Asset Manager Shorts'],
            "Asset Manager Spreads":cotEURO.iloc[0]['Asset Manager Spreads'],
            "Leveraged Funds Longs":cotEURO.iloc[0]['Leveraged Funds Longs'],
            "Leveraged Funds Shorts":cotEURO.iloc[0]['Leveraged Funds Shorts'],
            "Leveraged Funds Spreads":cotEURO.iloc[0]['Leveraged Funds Spreads'],
            "Other Reportable Longs":cotEURO.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotEURO.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotEURO.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotEURO.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotEURO.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotEURO.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotEURO.iloc[0]['Non Reportable Shorts']
               
        }, index=[0])
COT_Currencies=COT_Currencies.append(newRow)[COT_Currencies.columns.tolist()]

#Commitment of Traders - JAPANESE YEN (CME) - Futures and Options (097741)
cotYEN =quandl.get('CFTC/097741_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {    "Date":date,   
            "Ticker":"JPY",
            "Open Interest":cotYEN.iloc[0]['Open Interest'],
            "Dealer Longs":cotYEN.iloc[0]['Dealer Longs'],
            "Dealer Shorts":cotYEN.iloc[0]['Dealer Shorts'],
            "Dealer Spreads":cotYEN.iloc[0]['Dealer Spreads'],
            "Asset Manager Longs":cotYEN.iloc[0]['Asset Manager Longs'],
            "Asset Manager Shorts":cotYEN.iloc[0]['Asset Manager Shorts'],
            "Asset Manager Spreads":cotYEN.iloc[0]['Asset Manager Spreads'],
            "Leveraged Funds Longs":cotYEN.iloc[0]['Leveraged Funds Longs'],
            "Leveraged Funds Shorts":cotYEN.iloc[0]['Leveraged Funds Shorts'],
            "Leveraged Funds Spreads":cotYEN.iloc[0]['Leveraged Funds Spreads'],
            "Other Reportable Longs":cotYEN.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotYEN.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotYEN.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotYEN.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotYEN.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotYEN.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotYEN.iloc[0]['Non Reportable Shorts']
               
        }, index=[1])
COT_Currencies=COT_Currencies.append(newRow)[COT_Currencies.columns.tolist()]

#Commitment of Traders - BRITISH POUND STERLING (CME) - Futures and Options (096742)
cotGBP =quandl.get('CFTC/096742_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {    "Date":date,   
            "Ticker":"GBP",
            "Open Interest":cotGBP.iloc[0]['Open Interest'],
            "Dealer Longs":cotGBP.iloc[0]['Dealer Longs'],
            "Dealer Shorts":cotGBP.iloc[0]['Dealer Shorts'],
            "Dealer Spreads":cotGBP.iloc[0]['Dealer Spreads'],
            "Asset Manager Longs":cotGBP.iloc[0]['Asset Manager Longs'],
            "Asset Manager Shorts":cotGBP.iloc[0]['Asset Manager Shorts'],
            "Asset Manager Spreads":cotGBP.iloc[0]['Asset Manager Spreads'],
            "Leveraged Funds Longs":cotGBP.iloc[0]['Leveraged Funds Longs'],
            "Leveraged Funds Shorts":cotGBP.iloc[0]['Leveraged Funds Shorts'],
            "Leveraged Funds Spreads":cotGBP.iloc[0]['Leveraged Funds Spreads'],
            "Other Reportable Longs":cotGBP.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotGBP.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotGBP.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotGBP.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotGBP.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotGBP.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotGBP.iloc[0]['Non Reportable Shorts']
               
        }, index=[2])
COT_Currencies=COT_Currencies.append(newRow)[COT_Currencies.columns.tolist()]

#Commitment of Traders - AUSTRALIAN DOLLAR (CME) - Futures and Options (232741)
cotAUD =quandl.get('CFTC/232741_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {    "Date":date,   
            "Ticker":"AUD",
            "Open Interest":cotAUD.iloc[0]['Open Interest'],
            "Dealer Longs":cotAUD.iloc[0]['Dealer Longs'],
            "Dealer Shorts":cotAUD.iloc[0]['Dealer Shorts'],
            "Dealer Spreads":cotAUD.iloc[0]['Dealer Spreads'],
            "Asset Manager Longs":cotAUD.iloc[0]['Asset Manager Longs'],
            "Asset Manager Shorts":cotAUD.iloc[0]['Asset Manager Shorts'],
            "Asset Manager Spreads":cotAUD.iloc[0]['Asset Manager Spreads'],
            "Leveraged Funds Longs":cotAUD.iloc[0]['Leveraged Funds Longs'],
            "Leveraged Funds Shorts":cotAUD.iloc[0]['Leveraged Funds Shorts'],
            "Leveraged Funds Spreads":cotAUD.iloc[0]['Leveraged Funds Spreads'],
            "Other Reportable Longs":cotAUD.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotAUD.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotAUD.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotAUD.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotAUD.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotAUD.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotAUD.iloc[0]['Non Reportable Shorts']
               
        }, index=[3])
COT_Currencies=COT_Currencies.append(newRow)[COT_Currencies.columns.tolist()]


#Commitment of Traders - CANADIAN DOLLAR (CME) - Futures and Options (090741)
cotCAD =quandl.get('CFTC/090741_FO_ALL', start_date=date.strftime('%Y-%m-%d'))
newRow= pd.DataFrame (
        {    "Date":date,   
            "Ticker":"CAD",
            "Open Interest":cotCAD.iloc[0]['Open Interest'],
            "Dealer Longs":cotCAD.iloc[0]['Dealer Longs'],
            "Dealer Shorts":cotCAD.iloc[0]['Dealer Shorts'],
            "Dealer Spreads":cotCAD.iloc[0]['Dealer Spreads'],
            "Asset Manager Longs":cotCAD.iloc[0]['Asset Manager Longs'],
            "Asset Manager Shorts":cotCAD.iloc[0]['Asset Manager Shorts'],
            "Asset Manager Spreads":cotCAD.iloc[0]['Asset Manager Spreads'],
            "Leveraged Funds Longs":cotCAD.iloc[0]['Leveraged Funds Longs'],
            "Leveraged Funds Shorts":cotCAD.iloc[0]['Leveraged Funds Shorts'],
            "Leveraged Funds Spreads":cotCAD.iloc[0]['Leveraged Funds Spreads'],
            "Other Reportable Longs":cotCAD.iloc[0]['Other Reportable Longs'],
            "Other Reportable Shorts":cotCAD.iloc[0]['Other Reportable Shorts'],
            "Other Reportable Spreads":cotCAD.iloc[0]['Other Reportable Spreads'],
            "Total Reportable Longs":cotCAD.iloc[0]['Total Reportable Longs'],
            "Total Reportable Shorts":cotCAD.iloc[0]['Total Reportable Shorts'],
            "Non Reportable Longs":cotCAD.iloc[0]['Non Reportable Longs'],
            "Non Reportable Shorts":cotCAD.iloc[0]['Non Reportable Shorts']
               
        }, index=[4])
COT_Currencies=COT_Currencies.append(newRow)[COT_Currencies.columns.tolist()]



# Convert the dataframe to an XlsxWriter Excel object.
COT_Currencies.to_excel(writer, sheet_name='Currencies')









# Close the Pandas Excel writer and output the Excel file.
writer.save()









