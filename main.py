import pandas as pd
import numpy as np
#import datetime
from datetime import datetime
from dateutil.parser import parse

# Enter in the CSVs you want to process:
# this is for the power values:

# This is purely for the timestamp, concatenate later:
df = pd.read_csv('14545_house_profile_10_.csv', header=None)

# Give labels
df.columns =['Timestamp', 'Power']


# Make sure Timestamp type is datetime
df['Timestamp'] = df['Timestamp'].astype('datetime64')

# Set DateTime column as index
df.set_index('Timestamp', inplace=True)

# 300s stands for 5 min offset, add flag "closed='right' " to get it to do it down instead of up:
df = df.resample('300s', label='right',closed='right').mean()


# Unindexing timestamp col:
df.reset_index(level=0, inplace=True)

for i in range(len(df)):
    # Check each value for nan
    if np.isnan(df.iloc[i,1]):
        df.iloc[i,1] = df.iloc[i-1,1]
print(df)

#print(df['Timestamp'].dtypes)
df['Timestamp'] = df['Timestamp'].mask(df['Timestamp'].dt.year == 2013, df['Timestamp'] + pd.offsets.DateOffset(year=2021))
#print(df)

# Add missing rows to df and use last power value:
df.loc[len(df.index)] = ['2021-01-12 23:50:00', df.iloc[-1,1]]
df.loc[len(df.index)] = ['2021-01-12 23:55:00', df.iloc[-1,1]]
print(df)


# Printing out sampled CSV with removed headers (col labels) and keeping the index (timestamp col):
df.to_csv('14545_house_profile_10.csv', header=False, index=False)