import requests
from bs4 import BeautifulSoup


url = 'https://stage.ruscore.ru/2026-02-02'

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

h1 = soup.find('h1')

print(h1)
