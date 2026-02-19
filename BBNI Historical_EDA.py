# EDA BBNI JK Historical Price

# %% Load Dataset
import pandas as pd
df_clean = pd.read_pickle("E:\PROJECT ANALYST\BBNI_clean.pkl")
print(df_clean.head())

# %% Yearly Tren Historical Price
# Yearly Historical Price
import matplotlib.pyplot as plt

plt.figure()
plt.plot(df_clean['adjclose'])
plt.title('Historical Price of BBNI')
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()

yearly_avg = df_clean['adjclose'].resample('Y').mean()
print('Maximum Historical Price Mean:', yearly_avg.max())
plt.plot(yearly_avg)
plt.title('Yearly Average of BBNI')
plt.show()

yearly_last = df_clean['adjclose'].resample('Y').last()
plt.plot(yearly_last)
plt.title('Yearly Last of BBNI')
plt.show()

# %% Tren Moving Average
# Moving Average
df_clean['MA50'] = df_clean['adjclose'].rolling(50).mean()
df_clean['MA200'] = df_clean['adjclose'].rolling(200).mean()

plt.figure()
plt.plot(df_clean['MA50'])
plt.plot(df_clean['MA200'])
plt.title('Moving Average')
plt.show()

# %% Volatility
#Volatility
df_clean['daily_return'] = df_clean['adjclose'].pct_change()
df_clean['volatility_20d'] = df_clean['daily_return'].rolling(20).std()
print(df_clean.head())

plt.figure()
plt.plot(df_clean['daily_return'])
plt.title('Volatility')
plt.show()

plt.figure()
plt.plot(df_clean['volatility_20d'])
plt.title('volatility 20 day')
plt.show()

# %% Annual Return
# Annual Return
annual_return = df_clean['adjclose'].resample('Y').last().pct_change()
print(annual_return)

annual_return.index = annual_return.index.year
plt.figure()
plt.bar(annual_return.index, annual_return.values)
plt.title("Annual Return Value")
plt.show()

# Create Annual Return Table
yearly_df = df_clean['adjclose'].resample('Y').last().to_frame()
yearly_df['annual_return'] = yearly_df['adjclose'].pct_change()
yearly_df.index = yearly_df.index.year
print(yearly_df)

yearly_df.to_csv('Annual_Return.csv')

# %% The stabilition between Price and Volume
# Volume MA
df_clean['volume_ma20'] =df_clean['volume'].rolling(20).mean()

fig, ax1 = plt.subplots()
ax1.plot(df_clean['adjclose'])
ax1.set_ylabel('Price')

ax2 = ax1.twinx()
ax2.plot(df_clean['volume_ma20'])
ax2.set_ylabel('Volume MA20')

plt.title('Price VS Volume BBNI')
plt.show()

df_clean[['adjclose','volume']].corr()

# %% Yearly Volume (Likuiditas)
# Likuiditas
yearly_volume = df_clean['volume'].resample('Y').mean()
plt.plot(yearly_volume)
plt.title('Yearly Volume')
plt.show()

print(yearly_volume)

# %% Yearly Total Volume (Likuiditas)
yearly_total_volume = df_clean['volume'].resample('Y').sum()
print(yearly_total_volume)

# %% Up and Down Volume
df_clean['price_change'] = df_clean['adjclose'].diff()

volume_up = df_clean[df_clean['price_change']>0]['volume'].mean()
volume_down = df_clean[df_clean['price_change']<0]['volume'].mean()

print('Mean when volume up:', volume_up)
print('Mean when volume down:', volume_down)

# %% Maximum Drowdown 
# Drawdown
df_clean['running_max'] = df_clean['adjclose'].cummax()
df_clean['drawdown'] = (df_clean['adjclose']-df_clean['running_max'])/df_clean['running_max']
max_drawdown = df_clean['drawdown'].min()
print('Maximum Drawdown:', max_drawdown)
print(df_clean.head())

# %% Save Data
df_EDA = df_clean.copy()
df_EDA.reset_index().to_csv('BBNI_EDA.csv', index=False)

# %%
