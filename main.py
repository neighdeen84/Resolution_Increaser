import pandas as pd
import numpy as np
import datetime

# Enter in the CSVs you want to process:
# this is for the power values:

# This is purely for the timestamp, concatenate later:
df = pd.read_csv('14545_house_profile_1.csv', header=None)

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

# Printing out sampled CSV with removed headers (col labels) and keeping the index (timestamp col):
df.to_csv('Resampled.csv', header=False, index=False)