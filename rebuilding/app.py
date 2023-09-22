import pandas as pd 
import camelot 

tables = camelot.read_pdf('Credentials.pdf', pages='1')
print(tables)

simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
len(simpsons)
simpsons[1]

pd.read_csv('https://www.stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2023-quarter/Download-data/business-employment-data-june-2023-quarter.zip')


workData = pd.read_csv('https://www.stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2023-quarter/Download-data/business-employment-data-june-2023-quarter.zip')

workData.rename(columns={'Data_value':'DataSet',
'Period':'time'}, inplace=True)

pd.read_csv('https://www.stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2023-quarter/Download-data/business-employment-data-june-2023-quarter.zip')
