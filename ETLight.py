import pandas as pd
df = pd.DataFrame()
sheet_id = ''
sheet_name = ''
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
df = pd.read_csv(url)
df.columns = map(str.title, df.columns)
df.columns = df.columns.str.replace(' ','_')
df.columns = df.columns.str.replace('[^a-zA-Z_]', '', regex=True)
df = df.replace('[^0-9a-zA-Z,_-]+', ' ', regex=True)
display(df)
df.to_csv('my_file.csv', index=False, quoting=csv.QUOTE_ALL, quotechar='"', encoding='utf-8')
