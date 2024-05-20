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
    print(filename)
    print(extention)

    if extention == "js":
        subprocess.run(["node", file], check=True, capture_output=True, text=True)
    elif extention == "py":
        # subprocess.run(["python", file], check=True, capture_output=True, text=True)
        
        result = subprocess.run(["python", file], capture_output=True, text=True, check=True)
        #
        print(result.stdout)
        print(result.stderr)
    elif extention == "ipynb":
        subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", file], check=True, capture_output=True)
    else:
        print("Subprocess could not done.") 
        print(filename, "is the problem.")
        break

    print(filename, "run.")