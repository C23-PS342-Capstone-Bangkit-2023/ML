
import requests
from bs4 import BeautifulSoup
import csv

def ambil_data1(link):
  url = link

  response = requests.get(url)
  html = response.content

  soup = BeautifulSoup(html, 'html.parser')
  table = soup.find_all('table')[18]


  rows = []
  for row in table.find_all('tr'):
    cells = []
    for cell in row.find_all('td'):
        cells.append(cell.text)
    rows.append(cells)


  with open('data1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

def ambil_data2(link):
  url = link

  response = requests.get(url)
  html = response.content

  soup = BeautifulSoup(html, 'html.parser')
  table = soup.find_all('table')[18]


  rows = []
  for row in table.find_all('tr'):
    cells = []
    for cell in row.find_all('td'):
        cells.append(cell.text)
    rows.append(cells)


  with open('data2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

ambil_data1('https://www.andrafarm.co.id/_andra.php?_i=daftar-tkpi&jobs=&perhal=600&urut=1&asc=0000000000&sby=&no1=2&knama=')
ambil_data2('https://www.andrafarm.co.id/_andra.php?_i=daftar-tkpi&jobs=&perhal=600&urut=1&asc=0000000000&sby=&no1=1&no2=600&kk=2#Tabel%20TKPI')