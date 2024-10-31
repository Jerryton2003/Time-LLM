import pandas as pd

# data_path = 'Alice_Springs_2023.csv'
# target = '96_DKA_MasterMeter1_Active_Power'
data_path = '96-Site_DKA-MasterMeter1.csv'
target = 'Active_Power'

data = pd.read_csv(data_path)
data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)
data.interpolate(method='linear', inplace=True)
data = data.dropna()  # 移除仍然存在的NaN值

# 提取逐小时索引和逐小时功率
# data_index = data.index.hour
# data_hourly = data[target].resample('h').mean()
data_resampled = data.resample('h').mean()
data_hourly = data_resampled[target]
# data_index = data_resampled.index

start_date = '2016/1/1 0:00:00'
end_date = '2018/1/1 0:00:00'
mask = (data_hourly.index >= start_date) & (data_hourly.index <= end_date)
data_hourly = data_hourly.loc[mask]

start_date = pd.to_datetime('2016/1/1 00:00:00')
end_date = pd.to_datetime('2018/1/1 00:00:00')

# Mask that only includes dates within the range
mask = (data_hourly.index >= start_date) & (data_hourly.index < end_date)

# Apply the mask
data_hourly = data_hourly.loc[mask]

df_new = pd.DataFrame()

df_new['date'] = data_hourly.index                               # use mask filtered index
df_new['date'] = df_new['date'].dt.strftime("%Y/%m/%d %H:%M:%S") # format datetime
df_new['hourly_data'] = data_hourly.values                       # use masked values

df_new.to_csv('P_DKASC.csv', index=False)                        # save correctly into csv
