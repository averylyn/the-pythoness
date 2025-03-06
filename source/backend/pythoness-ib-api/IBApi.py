from ibapi.client import *
from ibapi.wrapper import *
import pandas as pd

class IBApi(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = []

    def nextValidId(self, orderId: OrderId):
        print("Next Valid Id: ", orderId)

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        print("ContractDetails: ", contractDetails)

    def contractDetailsEnd(self, reqId: int):
        print("ContractDetailsEnd")

    def historicalData(self, reqId: int, bar: BarData):
        self.data.append([
            bar.date  , bar.open   , bar.high    , bar.low     ,
            bar.close , bar.volume , bar.average , bar.barCount])

    def historicalDataEnd(self, reqId: int, start: str, end: str):
        df = pd.DataFrame(self.data, columns=[
            "Date", "Open", "High", "Low", "Close", "Volume", "Average", "BarCount"])
        df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d  %H:%M:%S')
        df.set_index('Date', inplace=True)
        print("[reqId:" + str(reqId) + "] " + "creating dataframe for historicalData...")
        print(df)
        return super().historicalDataEnd(reqId, start, end)

    def historicalTicksBidAsk(self, reqId: int, ticks: ListOfHistoricalTick, done: bool):
        data = []
        for tick in ticks:
            data.append([tick.time, tick.priceBid, tick.priceAsk, tick.sizeBid, tick.sizeAsk])
        df = pd.DataFrame(data, columns=["Time", "PriceBid", "PriceAsk", "SizeBid", "SizeAsk"])
        df.set_index('Time', inplace=True)
        print("[reqId:" + str(reqId) + "] " + "creating dataframe for historicalTicksBidAsk...")
        print(df)

    def mktDepthExchanges(self, depthMktDataDescriptions:ListOfDepthExchanges):
        super().mktDepthExchanges(depthMktDataDescriptions)
        data = []
        for desc in depthMktDataDescriptions:
            data.append([desc.exchange, desc.secType, desc.listingExch, desc.serviceDataType, desc.aggGroup])
        df = pd.DataFrame(data, columns=["Exchange", "SecType", "ListingExch", "ServiceDataType", "AggGroup"])
        print("creating dataframe for mktDepthExchanges...")
        print(df)

    def error(
        self, reqId: TickerId, errorCode : int, errorString : str , advancedOrderRejectJson=""):
        print(reqId, errorCode, errorString, advancedOrderRejectJson)