
import IBApi as ib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

port = 4002


api = ib.IBApi()
api.connect("127.0.0.1", port, 0)

api_thread = threading.Thread(target=api.run, daemon=True)
api_thread.start()

