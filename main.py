import pandas as pd
from random import randint
from flask import Flask, render_template

df_words = pd.read_csv("core_files/german_words.csv")
list = []
for i in range(len(df_words)):
    list.append(0)
df_words["times_correct"] = list


print(df_words)
"""index = randint(0, len(df_words)-1)
row = df_words.iloc[randint(0,index)].tolist()
print(row)
row[2] = 2
df_words.iloc[randint(0,index)] = row
row = row = df_words.iloc[randint(0,index)]
print(row[2])"""