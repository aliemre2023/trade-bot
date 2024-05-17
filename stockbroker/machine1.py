from wallet import Wallet
import pandas as pd

my_wallet = Wallet("Mr. Machine")

#my_wallet.add_money(10000) 
# 10000 tl added in 18may 02:16


trust_values = pd.read_csv("scraper/data/trust_values.csv")

# bought portion
for index, row in trust_values[::-1].iterrows():
    value_row = row["value"]
    code_row = row["code"]

    if(value_row > 50):
        my_wallet.buy(code_row + ".IS", value_row/5) 

# sell portion
for company, stock in my_wallet.portfolio.items():
    company = company.split(".")[0]

    trust_value = trust_values.loc[trust_values.code == company, "value"].index[0]
    
    if(trust_value < 50):
        my_wallet.sell(company+".IS", stock)



my_wallet.show_asset()
my_wallet.save_wallet()