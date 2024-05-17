import yfinance as yf
import pandas as pd

class Wallet:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.portfolio = {}
        self.load_wallet() # wallet be loaded if trader exist

    def load_wallet(self):
        bank = pd.read_csv("stockbroker/bank.csv")

        for index,row in bank.iterrows():
            trader = row["Trader"]
            money = row["Money"]
            self.money = money
            
            if(trader == self.name):
                for company, stock in row.items():
                    if(company != "Trader" or company != "Money"):
                        self.portfolio[company + ".IS"] = stock
    
    def save_wallet(self):
        bank = pd.read_csv("stockbroker/bank.csv")

        portfolio_only_code = dict()
        for key,value in self.portfolio.items():
            key = key.split(".")[0]
            portfolio_only_code[key] = value

        if ((len(bank["Trader"].values) == 0) or (self.name not in bank["Trader"].values)):
            new_row = dict()
            new_row["Trader"] = self.name
            
            for company in bank.columns:
                company = company.split(".")[0]
                #print(company)
                if(company != "Trader" and company != "Money"):  
                    if company in portfolio_only_code.keys():
                        #print("girdim")
                        new_row[company] = portfolio_only_code[company] # 0 if not exist
                    else:
                        new_row[company] = 0
            bank.loc[len(bank)] = new_row
            

        # if trader already exist
        else:       

            for company, stock in portfolio_only_code.items():
                bank[company] = stock
        
        bank.loc[bank["Trader"] == self.name, "Money"] = self.money

        bank.to_csv("stockbroker/bank.csv", index=False)
    
                


            
    def add_money(self, money):
        self.money += money
    
    def buy(self, company, unit):
        cmp = yf.Ticker(str(company))
        last10days = cmp.history(period="10d")

        if len(last10days) == 0:
            print("No data available for", company)
            print(company, " was not bougthed")
            return
        per_value = last10days["Close"][-1]

        for _ in range(unit):
            if(self.money >  per_value):
                self.money -=  per_value

                if(company in self.portfolio):
                    self.portfolio[company] += 1
                else:
                    self.portfolio[company] = 1
    
    def sell(self, company, unit):
        cmp = yf.Ticker(str(company))
        last10days = cmp.history(period="10d")
        if len(last10days) == 0:
            print("No data available for", company)
            return
        per_value = last10days["Close"][-1]

        if(company in self.portfolio):
            if(self.portfolio[company] - unit >= 0):
                self.money += unit * per_value
                self.portfolio[company] -= unit 
            else:
                self.money += self.portfolio[company] * per_value
                self.portfolio[company] = 0
        
    def show_asset(self):
        print("Trader: ", self.name)

        total = self.money
        for key, value in self.portfolio.items():
            if(value != 0 and key != "Trader.IS" and key != "Money.IS"):
                cmp = yf.Ticker(key)
                last10days = cmp.history(period="10d")
                if len(last10days) == 0:
                    print("No data available for", key)
                    
                else:
                    per_value = last10days["Close"][-1]
                    total += value * per_value
                #print(key)

                print(f"{key}: {value}")
        
        print("Total asset: ", total)