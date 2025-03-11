from ibapi.client import *
from ibapi.wrapper import *
import pandas as pd

class IBClient(EClient, EWrapper):

    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId: TickerId, errorCode : int, errorString : str , advancedOrderRejectJson=""):
        s = pd.Series(locals(), name="IBAPI_ERROR")
        print(s)

    def nextValidId(self, orderId: OrderId):
        s = pd.Series(locals(), name="NEXT_VALID_ID")
        print(s)