import pandas as pd
csv_path = 'results_linetoday.csv'
df = pd.read_csv('results_linetoday.csv')

linetodaydata = df.T

saving = linetodaydata.to_csv('resultstranspose.csv', index=False)
saving