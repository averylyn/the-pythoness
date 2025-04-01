from ibapi.client import *
import Client as cl
import pandas as pd
import matplotlib.pyplot as plt
import threading
import time
import debugpy
from ibapi.contract import Contract
from datetime import datetime, timezone

if __name__ == "__main__":
    client = cl.Client()
    client.connect("ib-gateway", port=4004, clientId=0)
    client_thread = threading.Thread(target=client.run, daemon=True)
    client_thread.start()
    breakpoint()

    contract = Contract()
    contract.symbol = "NQ"
    contract.secType = "FUT"
    contract.exchange = "CME"
    contract.currency = "USD"
    contract.lastTradeDateOrContractMonth = "202504"
    breakpoint()

    client.reqIds(-1)
    time.sleep(5)
    breakpoint()

    client.reqContractDetails(client.next_valid_id, contract) #-1 is required for api for some reason
    time.sleep(5)
    breakpoint()

    for node in client.messages:
        print(repr(node))
        breakpoint()

    client.disconnect()