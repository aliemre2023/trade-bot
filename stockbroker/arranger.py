"""
It will prepare bank.csv in the wanted form,
if it will be runned acounts will be deleted
"""

import pandas as pd

bist100 = pd.read_csv("bist100/bist100.csv", delimiter=";")

column_list = ["Trader"] + ["Money"] + bist100["code"].tolist()
bank = pd.DataFrame(columns=column_list)

bank.to_csv("stockbroker/bank.csv", index=False)
