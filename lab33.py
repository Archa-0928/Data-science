import pandas as pd
data = {
    "Name": ["raj","Bob","Eva"],
    "mark": [88,70,85,]
}
df = pd.DataFrame(data)
filtered_df = df[df["mark"]>80]
print(filtered_df)
sorted_df = df.sort_values(by=["mark"],ascending=False)
print("\n students marks sorted")
print(sorted_df)

