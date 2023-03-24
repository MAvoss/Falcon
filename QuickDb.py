import sqlite3
import pandas as pd

# establish a connection to the SQLite database
conn = sqlite3.connect('mydatabase.db')

# create a pandas DataFrame
df = pd.DataFrame()
sheet_id = '1bNuRvFZHQGvprpVO1Vag0LgJRkSzjkiZV4XSrvzcVLQ'
sheet_name = 'Sheet1'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
df = pd.read_csv(url)
df.columns = map(str.title, df.columns)
df.columns = df.columns.str.replace(' ','_')
df.columns = df.columns.str.replace('[^a-zA-Z_]', '', regex=True)
df = df.replace('[^0-9a-zA-Z,_-]+', ' ', regex=True)
display(df)

# write the DataFrame to the database table
df.to_sql('us_ships', conn, if_exists='replace', index=False)

# close the connection
conn.close()

# establish a connection to the SQLite database
conn = sqlite3.connect('mydatabase.db')

# execute a SELECT query
query = "SELECT * FROM us_ships"
results = pd.read_sql_query(query, conn)

# close the connection
conn.close()

# print the results as a pandas DataFrame
print(results)
