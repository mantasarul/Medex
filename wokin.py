import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

first_page = requests.get('https://medex.com.bd/brands').text
soup = BeautifulSoup(first_page, 'lxml')

# def scrape(diya):
#     medex = diya.find_all('div', class_="row -data-row")
#     for med in medex:
#         mantasarul = med.find_all('div', class_="col-xs-12")
#         for mim in mantasarul:
#             misty = mim.text
#             print(f"{misty}")
#             with open("C:\\Users\\manta\\Desktop\\Django Repository\\Medex\\medex.txt") as nova:
#                 nova.write(f"{misty}")
#                 nova.write(f"\n")

# scrape(first_soup)

# for x in range[2,694]:
#     dynamic_page = requests.get("https://medex.com.bd/brands?page={x}").text
#     second_soup = BeautifulSoup(dynamic_page, 'lxml')
#     scrape(second_soup)

medex = soup.find_all('div', class_="row -data-row")
for med in medex:
    mantasarul = med.find_all('div', class_="col-xs-12")
    for mim in mantasarul:
        misty = mim.text
        print(f"{misty}")
        with open("C:\\Users\\manta\\Desktop\\Django Repository\\Medex\\medex.txt") as nova:
            nova.write(f"{misty}")
            nova.write(f"\n")

