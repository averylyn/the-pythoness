import IBApi as ib
import ibapi.contract as contract
import pandas as pd
import matplotlib.pyplot as plt
import threading
import time
from datetime import datetime, timezone

if __name__ == "__main__":
    port = 4002
    client_id = 1

    api = ib.IBApi()
    api.connect("127.0.0.1", port, client_id)

    api_thread = threading.Thread(target=api.run, daemon=True)
    api_thread.start()

    contract = contract.Contract()
    contract.symbol = "NQ"
    contract.secType = "FUT"
    contract.exchange = "CME"
    contract.currency = "USD"
    contract.lastTradeDateOrContractMonth = "202503"

    print(datetime.now(timezone.utc))

    api.reqMktDepthExchanges()
    time.sleep(5)

    api.reqHistoricalData(1, contract, "", "1 D", "1 min", "TRADES", 0, 1, False, [])
    time.sleep(5)

    api.reqHistoricalTicks(2, contract, "20250304-12:00:00", "", 3, "BID_ASK", 0, False, [])
    time.sleep(5)