import pandas as pd

data_path = 'Alice_Springs_2023.csv'
target = '96_DKA_MasterMeter1_Active_Power'

data = pd.read_csv(data_path)
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)
data.interpolate(method='linear', inplace=True)

# 提取逐小时索引和逐小时功率
# data_index = data.index.hour
# data_hourly = data[target].resample('h').mean()
data_resampled = data.resample('h').mean()
data_hourly = data_resampled[target]
data_index = data_resampled.index

# 创建新dataframe存储两列
df_new = pd.DataFrame()

df_new['date'] = data_index.strftime("%Y/%m/%d %H:%M:%S")
df_new['hourly_data'] = data_hourly.values

df_new.to_csv('P_Alice_Springs_2023.csv.csv', index=False)
