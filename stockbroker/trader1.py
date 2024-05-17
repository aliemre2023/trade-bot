from wallet import Wallet

"""
import pandas as pd

trust_values = pd.read_csv("scraper/data/trust_values.csv")
buyable_cmp = pd.DataFrame(columns=["code","value"])

for index, row in trust_values[::-1].iterrows():
    value_row = row["value"]
    code_row = row["code"]

    if(value_row > 60):
        buyable_cmp.loc[len(buyable_cmp)] = {"code": f"{code_row}.IS", "value": value_row}

"""
#########################################
my_wallet = Wallet("Mr. Machine")

my_wallet.add_money(1000)

my_wallet.buy("GENIL.IS", 15)
my_wallet.buy("EREGL.IS", 10)

my_wallet.show_asset()
my_wallet.save_wallet()



