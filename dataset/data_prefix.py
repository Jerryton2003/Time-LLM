import pandas as pd

# data_path = 'Alice_Springs_2023.csv'
# target = '96_DKA_MasterMeter1_Active_Power'
data_path = '96-Site_DKA-MasterMeter1.csv'
target = 'Active_Power'

data = pd.read_csv(data_path)
data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)
data.interpolate(method='linear', inplace=True)

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

# # 创建新dataframe存储两列
# df_new = pd.DataFrame()
#
# df_new['date'] = data_index.strftime("%Y/%m/%d %H:%M:%S")
# df_new['hourly_data'] = data_hourly.values
#
# df_new = df_new.transpose()
# # 重新设置索引，并将原先的数据放到新的列中
# df_new = df_new.reset_index()
#
# # 将第一行数据作为表头
# df_new.columns = df_new.iloc[0]
# df_new = df_new[1:]
#
# # df_new.to_csv('P_Alice_Springs_2023_1.csv', index=False)
# df_new.to_csv('P_DKASC', index=False)

# ...
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
