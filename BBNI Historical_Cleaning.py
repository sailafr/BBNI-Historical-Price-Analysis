# Data Cleaning BBNI JK Historical Price

# %% Import Library
import pandas as pd

# %% Load Dataset
df = pd.read_csv("E:\PROJECT ANALYST\BBNI.JK.csv")
print(df.head())

# %% Cek Statistic and Data Type
print(df.describe())
print(df.info())
print(df.shape)

# %% Data Duplicate
print('Duplicate Data:', df.duplicated().sum())

# %% Change Datetime
df['Date'] = pd.to_datetime(df['Date'])
df.info()
df.set_index('Date', inplace=True)

# %% Save Data
df_clean = df.copy()
df_clean.to_pickle("BBNI_clean.pkl")