import os
import pandas as pd
from data.keywords import positive, negative
import re
import collections


bist100 = pd.read_csv("bist100/bist100.csv", delimiter=";")
bist100 = bist100.drop(columns=["Unnamed: 5"])

name_dict = dict()
trust_dict = dict()
for index, row in bist100.iterrows():
    code = row["code"]
    trust_dict[code] = 0

    name_list = list()
    name_list.append(code)
    for name in re.split(r'\s+|\|', row["company"]):
        name_list.append(name)
    name_dict[code] = name_list



for date in os.listdir("scraper/news"):
    for agenta in os.listdir(f"scraper/news/{date}"):
        f = open(f"scraper/news/{date}/{agenta}")
        new_list = f.read().split("-"*50)
        trust = 0
        for new in new_list:
            will_evaluated = list()
            for key, values in name_dict.items():
                for name in values:
                    if name in new:
                        will_evaluated.append(key)
            for pos in positive:
                if pos in new:
                    trust += 1
            for neg in negative:
                if neg in new:
                    trust -= 1
            
            for company_code in will_evaluated:
                trust_dict[company_code] += trust 
        


trust_output = open("scraper/data/trust_values.csv", "w")

trust_output.write("code,value\n")

sorted_dict = {k: v for k, v in sorted(trust_dict.items(), key=lambda item: item[1])}
for key, value in sorted_dict.items():
    trust_output.write(f"{key},{value}\n")
        

