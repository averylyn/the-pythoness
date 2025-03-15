import IBClient as ibcl
import ibapi.contract as contract
import pandas as pd
import matplotlib.pyplot as plt
import threading
import time
from datetime import datetime, timezone

if __name__ == "__main__":
    port = 7499
    client_id = 0

    ibclient = ibcl.IBClient()
    ibclient.connect("ib-gateway", port, client_id)

    api_thread = threading.Thread(target = ibclient.run, daemon=True)
    api_thread.start()

    contract = contract.Contract()
    contract.symbol = "NQ"
    contract.secType = "FUT"
    contract.exchange = "CME"
    contract.currency = "USD"
    contract.lastTradeDateOrContractMonth = "202503"

    print(locals())

    ibclient.reqIds(0)