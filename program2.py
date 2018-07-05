import math
from typing import Optional, Any

import pandas as pd
import quandl
#from pandas import ExcelWriter
'''
df = quandl.get("WIKI/GOOGL")

print(df.head())

df_1=df.copy()  # type: dataframe


writer = pd.ExcelWriter('Google_Stock.xlsx')
df_1.to_excel(writer)
writer.save()
'''

df=pd.read_excel('Google_Stock.xlsx')
df.set_index('Date', inplace=True)
#print(df.head())

df_1=df.copy()
df_1 = df_1[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]

df_1['HL_PCT'] = (df_1['Adj. High'] - df_1['Adj. Low']) / df_1['Adj. Close'] * 100.0

df_1['PCT_change'] = (df_1['Adj. Close'] - df_1['Adj. Open']) / df_1['Adj. Open'] * 100.0

df_1 = df_1[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
#print(df_1.head())

forecast_col='Adj. Close'
df_1.fillna(-99999,inplace=True)

forecast_out = int(math.ceil(0.01 * len(df)))
df_1['label'] = df_1[forecast_col].shift(-forecast_out)

df_1.dropna(inplace=True)
print(df_1.head()) 