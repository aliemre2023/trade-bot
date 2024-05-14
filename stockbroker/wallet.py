import yfinance as yf

class Wallet:
    def __init__(self, money):
        self.money = money
        self.portfolio = dict()
    
    def buy(self, company, unit):
        cmp = yf.Ticker(str(company))
        last10days = cmp.history(period="10d")

        if len(last10days) == 0:
            print("No data available for", company)
            return
        per_value = last10days["Close"][-1]

        if(self.money > unit * per_value):
            self.money -= unit * per_value

            if(company in self.portfolio):
                self.portfolio[company] += unit
            else:
                self.portfolio[company] = unit
    
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
        total = self.money
        for key, value in self.portfolio.items():
            cmp = yf.Ticker(key)
            last10days = cmp.history(period="10d")
            if len(last10days) == 0:
                print("No data available for", key)
                return
            per_value = last10days["Close"][-1]
            total += value * per_value
            print(key)

            print(f"{key}: {value}")
        
        print("Total asset: ", total)
        
        

        
    
        
    