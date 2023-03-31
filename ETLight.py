import pandas as pd
from datetime import datetime
import pytz
import csv

df = pd.DataFrame()
sheet_id = '1bNuRvFZHQGvprpVO1Vag0LgJRkSzjkiZV4XSrvzcVLQ'
sheet_name = 'Sheet1'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
df = pd.read_csv(url)

# Check if a column is a timestamp
def is_timestamp(col):
    try:
        pd.to_datetime(col)
        return True
    except ValueError:
        return False

# Convert timestamp column to another timezone
def convert_timezone(col, src_timezone, dst_timezone):
    tz_src = pytz.timezone(src_timezone)
    tz_dst = pytz.timezone(dst_timezone)
    return pd.to_datetime(col, utc=True).dt.tz_convert(tz_dst).dt.tz_localize(None)

# Add column with today's date
today = datetime.today().strftime('%Y-%m-%d')
df[today] = pd.to_datetime(today)

# Detect timestamp columns and convert timezone
for col in df.columns:
    if is_timestamp(df[col]):
        df[f'{col}_local'] = convert_timezone(df[col], 'UTC', 'America/New_York')

# Format column names
df.columns = map(str.title, df.columns)
df.columns = df.columns.str.replace(' ','_')
df.columns = df.columns.str.replace('[^a-zA-Z_]', '', regex=True)

# Replace any non-alphanumeric characters with a space in the DataFrame values.
df = df.replace('[^0-9a-zA-Z,_-]+', ' ', regex=True)

# Display the DataFrame
display(df)

# Write the DataFrame to a CSV file with time zone conversion and today's date column
output_timezone = 'America/New_York'  # Output time zone
df.to_csv('my_file.csv', index=False, quoting=csv.QUOTE_ALL, quotechar='"', encoding='utf-8')

