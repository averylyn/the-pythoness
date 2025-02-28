from ibapi.client import *
from ibapi.wrapper import *
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

port = 4002

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = []

    def nextValidId(self, orderId: OrderId):
        mycontract = Contract()
        mycontract.conId = 265598
        mycontract.exchange = "SMART"
        
        self.reqHistoricalData(
            reqId=123,
            contract=mycontract,
            endDateTime="",
            durationStr= "2 D",
            barSizeSetting = "1 hour",
            whatToShow= "TRADES",
            useRTH=0,
            formatDate=1,
            keepUpToDate=False,
            chartOptions=[],
        )

    def historicalData(self, reqId: int, bar: BarData):
        self.data.append([
            bar.date, bar.open, bar.high, bar.low, bar.close,
            bar.volume, bar.average, bar.barCount
        ])

    def historicalDataEnd(self, reqId: int, start: str, end: str):
        df = pd.DataFrame(self.data, columns=[
            "Date", "Open", "High", "Low", "Close", "Volume", "Average", "BarCount"
        ])
        df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d  %H:%M:%S')
        df.set_index('Date', inplace=True)
        print("creating dataframe")
        print(df)
        
        return super().historicalDataEnd(reqId, start, end)

    def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
        print(reqId, errorCode, errorString, advancedOrderRejectJson)

app = TestApp()
app.connect("127.0.0.1", port, 1)
app.run()