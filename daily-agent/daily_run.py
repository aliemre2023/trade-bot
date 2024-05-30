import subprocess


if __name__ == "__main__":
        
    paths = [
        "/Users/aliemre2023/Desktop/github/trade-bot/scraper/html_extracter.js",
        "/Users/aliemre2023/Desktop/github/trade-bot/scraper/news_scraper.py",
        "/Users/aliemre2023/Desktop/github/trade-bot/scraper/evaluation.py",
        "/Users/aliemre2023/Desktop/github/trade-bot/stockbroker/trader1.py",
        "/Users/aliemre2023/Desktop/github/trade-bot/stockbroker/machine1.py",
        "/Users/aliemre2023/Desktop/github/trade-bot/stockbroker/machine2.py"
    ]

    for file in paths:
        filename = file.split("/")[-1]
        extention = filename.split(".")[-1]

        print(filename, "processing...")
        '''if extention == "js":
            subprocess.run(["/usr/local/bin/node", file])'''
        '''elif extention == "ipynb":
            subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", file])'''
        if extention == "py":
            subprocess.run(["python3", file])
        
        else:
            print("Subprocess could not done.") 
            print(filename, "is the problem.")
            #break

        print(filename, "processed.")