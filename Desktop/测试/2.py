import pandas as pd
import numpy as np

name = ['A']
df = pd.read_csv('fyx_chinamoney.csv', names=name)
list = []
arr = np.array(df)
for i in arr:
    for j in i:
        list.append(j)

print(list[:80])
print(list[80:160])
print(list[160:240])
print(list[240:320])
print(list[320:400])
print(list[400:480])
print(list[480:])
