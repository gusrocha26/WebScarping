import requests
from bs4 import BeautifulSoup
import csv




url = ('https://dados.gov.br/dataset/distribuicao-de-respiradores')


r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

params_link = soup.find('a', class_= "resource-url-analytics")
link = params_link.get('href')



r2 = requests.get(link)

with open ('teste.csv', 'wb') as f:
    f.write(r2.content)









