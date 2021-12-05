import requests
from bs4 import BeautifulSoup


html_text = requests.get('https://medex.com.bd/brands').text
soup = BeautifulSoup(html_text, 'lxml')

medex = soup.find_all('div', class_='row data-row')

for med in medex:
    # name = med.find('div', class_="data-row-top")
    # strength = med.find('div', class_="data-row-strength")
    # generic = med.find('div', class_="col-xs-12")
    all = med.find_all('div', class_="col-xs-12")
    # print(f"{name.text} {strength.text} {generic.text} ")
    for diya in all:
        print(diya.text)


# pip install selenium
# download the chrome driver