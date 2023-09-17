import pandas as pd

path = 'archive\cancer database.csv'
df = pd.read_csv(path) # replace with your own data source
print(df.head)