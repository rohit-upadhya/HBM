# -*- coding: utf-8 -*-

import pandas as pd
import json
import csv

with open('train_pos.json') as json_file:
    json_data = json.load(json_file)
    
data = json_data["data"]

texting = []

j = 0

for i in data:
    texting.append(i["text"])
    if(j>=2500):
        break
    j = j+1
given = {
    'text': texting
    }

df = pd.DataFrame(given)    

print(df.columns)

df.to_csv('ecthr_pos_text.csv', index=False)