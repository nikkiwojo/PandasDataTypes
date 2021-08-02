import pandas as pd
import numpy as np
from salescleanup import convert_currency
from salescleanup import convert_percent

df = pd.read_csv("https://github.com/chris1610/pbpython/blob/master/data/sales_data_types.csv?raw=True")

# Transforming data types
df['Customer Number'].astype('int')
df["Customer Number"] = df['Customer Number'].astype('int')
df['Active'].astype('bool')
df.astype({'Customer Number': 'int', 'Customer Name': 'str'}).dtypes

# Applying functions from salescleanup.py
df['2016'].apply(convert_currency)
df['2017'].apply(convert_currency)
df['2016'].apply(convert_currency) + df['2017'].apply(convert_currency)

# Assigning converted values back to the columns
df['2016'] = df['2016'].apply(convert_currency)
df['2017'] = df['2017'].apply(convert_currency)

# Handling invalid values
df["Jan Units"] = pd.to_numeric(df['Jan Units'], errors='coerce').fillna(0)
df["Start_Date"] = pd.to_datetime(df[['Month', 'Day', 'Year']])