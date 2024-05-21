import subprocess

paths = [
    "scraper/html_extracter.js",
    "scraper/news_scraper.py",
    "scraper/visualize_evaluation.ipynb",
    "stockbroker/trader1.py",
    "stockbroker/machine1.py",
    "stockbroker/machine2.py"
]

for file in paths:
    filename = file.split("/")[-1]
    extention = filename.split(".")[-1]

    print(filename, "processing...")
    if extention == "js":
        subprocess.run(["node", file])
    elif extention == "py":
        subprocess.run(["python", file])
    elif extention == "ipynb":
        subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", file])
    else:
        print("Subprocess could not done.") 
        print(filename, "is the problem.")
        break

    print(filename, "processed.")