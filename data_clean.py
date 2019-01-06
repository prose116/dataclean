import pandas as pd

df = pd.read_csv('/Users/python/Desktop/UT2019.csv', usecols=['Name', 'Extension', 'ToDeleteBy'])
df.drop_duplicates(subset=None, keep="first", inplace=True)  # removes duplicate entries
df.dropna(how='any', inplace=True)  # removes rows with no extension
df["Extension"] = df["Extension"].astype(int)  # changes float to integer
df.sort_values(['ToDeleteBy'],ascending=[True], inplace=True)   # sorts columns by date lowest to highest
df.to_csv('/Users/python/Desktop/to_be_deleted.csv', index=None)  # creates new file

print(df)  # print to screen for testing purposes
