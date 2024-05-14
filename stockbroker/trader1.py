from wallet import Wallet
import pandas as pd


my_wallet = Wallet(100)

trust_values = pd.read_csv("scraper/data/trust_values.csv")
buyable_cmp = pd.DataFrame(columns=["code","value"])

for index, row in trust_values[::-1].iterrows():
    value_row = row["value"]
    code_row = row["code"]

    if(value_row > 60):
        buyable_cmp.loc[len(buyable_cmp)] = {"code": f"{code_row}.IS", "value": value_row}

for index,row in buyable_cmp.iterrows():
    code = row["code"]
    my_wallet.buy(code, 10)

my_wallet.show_asset()



