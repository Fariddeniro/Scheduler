import this
import requests
from bs4 import BeautifulSoup
import pandas as pd

url2 = 'http://www.ieso.ca/-/media/files/ieso/uploaded/chart/\
        ontario_demand_multiday.xml?la=en'
resp = requests.get(url2)
soup = BeautifulSoup(resp.text, 'lxml')

infos = soup.select('DataSet')

Five_Min = infos[0].text
Actual = infos[1].text
Proj = infos[2].text


df = pd.DataFrame({'FiveMinDemand': Five_Min, 'Actual': Actual,
                  'Projected': Proj}, index=[0])
df_5 = df['FiveMinDemand'].str.split('\n\n', expand=True).T
df_5.columns = ['5Minute']
Act = df['Actual'].str.split('\n\n', expand=True).T

df = pd.concat([Act, df['Projected'].str.split('\n\n', expand=True).T], axis=1)
df.columns = ['Actual', 'Projected']

print(df[:169])
# df.to_csv(r'C:\Users\farid\Desktop\ActPrj.csv')

print(df_5[:1730])
# df_5.to_csv(r'C:\Users\farid\Desktop\FiveMin.csv')
