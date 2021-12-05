import requests
from bs4 import BeautifulSoup


# html_text = requests.get('https://medex.com.bd/brands').text
# soup = BeautifulSoup(html_text, 'lxml')

# medex = soup.find_all('div', class_='row data-row')

# for med in medex:
#     all = med.find_all('div', class_="col-xs-12")
#     for diya in all:
#         print(diya.text)

for x in range(2,694):
    url = 'https://medex.com.bd/brands?page=' + str(x)

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    medex = soup.find_all('div', class_='row data-row')

    for med in medex:
        all = med.find_all('div', class_="col-xs-12")
        for diya in all:
            print(diya.text)
