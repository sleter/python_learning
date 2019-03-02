import bs4 as bs
import pandas as pd

dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface', header=0)
for df in dfs:
    print(df)
