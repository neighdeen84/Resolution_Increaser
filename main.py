import pandas as pd
import numpy as np

# Enter in the CSVs you want to process:
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
    # Check each value for nan, if so set it equal to the value before it:
    if np.isnan(df.iloc[i,1]):
        df.iloc[i,1] = df.iloc[i-1,1]
print(df)

# Change the year from 2013 to 2021:
df['Timestamp'] = df['Timestamp'].mask(df['Timestamp'].dt.year == 2013, df['Timestamp'] + pd.offsets.DateOffset(year=2021))

# Add missing rows to df and use last power value:
# NOTE: this was only added because the original dataset ends at 23:45:00
df.loc[len(df.index)] = ['2021-01-12 23:50:00', df.iloc[-1,1]]
df.loc[len(df.index)] = ['2021-01-12 23:55:00', df.iloc[-1,1]]
print(df)


# Printing out sampled CSV with removed headers (col labels) and keeping the index (timestamp col):
df.to_csv('14545_house_profile_1_5_mins.csv', header=False, index=False)