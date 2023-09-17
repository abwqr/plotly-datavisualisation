import pandas as pd
import json
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
path = "data"
dir_list = os.listdir(path)
df = pd.DataFrame(columns = ["timestamp","temperature","humidity","pressure"])

for file in dir_list:
    path = 'data/'+file

    file1 = open(path, 'r')
    lines = file1.readlines()

    json_dict = json.loads(lines[0])
    

    df = df._append({"timestamp":json_dict["timestamp"],"temperature":json_dict["temperature"],"humidity":json_dict["humidity"],
                    "pressure":json_dict["pressure"]},ignore_index = True)
# print(df)
