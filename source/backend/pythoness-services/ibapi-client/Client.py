from ibapi.client import *
from ibapi.wrapper import *
import pandas as pd
import Node as nd

class Client(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.next_valid_id = int
        self.messages = []

    def nextValidId(self, orderId: OrderId):
        self.messages.append(nd.Node(locals().copy(), None, 0))
        self.next_valid_id = orderId

    def error(self, reqId: TickerId, errorCode : int, errorString : str , advancedOrderRejectJson=""):
        self.messages.append(nd.Node(locals().copy(), None, 0))

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        self.messages.append(nd.Node(locals().copy(), None, 0))
