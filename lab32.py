import pandas as pd

data = {
    "Name": ["raj", "Bob", "Eva"],
    "Age": [25, 30, 35],
    "city": ["ktm", "ekm", "app"]
}
df = pd.DataFrame(data)

df.to_csv("data.csv", index=False)
df = pd.read_csv("data.csv")

print("First row:")
print(df.head(1))

print("\nLast row:")
print(df.tail(1))