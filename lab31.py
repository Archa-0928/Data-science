import pandas as pd

data = {
    "Name": ["raj","Bob","Eva"],
    "Age": [25,30, 35,],
    "city":["ktm","ekm","app"]
}
df = pd.DataFrame(data)
print("ORIGINAL DATASET\n")
print(df)
