from wallet import Wallet

# to access parent folders childs
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from estimator.estimator1 import sequential_model

import pandas as pd

my_wallet = Wallet("Mr. Machine (sequential_model)")

#my_wallet.add_money(10000) 
# 10000 tl added in 18may 02:16


trust_values = pd.read_csv("scraper/data/trust_values.csv")

# bought portion
for index, row in trust_values[::-1].iterrows():
    value_row = row["value"]
    code_row = row["code"]

    if (value_row > 30):
        print(code_row, "evaluating...")
        if (sequential_model(code_row + ".IS")):
            my_wallet.buy(code_row + ".IS", value_row/3) 

# sell portion
for company, stock in my_wallet.portfolio.items():
    company = company.split(".")[0]

    trust_value = trust_values.loc[trust_values.code == company, "value"].index[0]
    
    if(trust_value < 50):
        my_wallet.sell(company+".IS", stock)



my_wallet.show_asset()
my_wallet.save_wallet()