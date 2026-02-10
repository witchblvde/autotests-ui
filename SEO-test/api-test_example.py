import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview Analytics) Chrome/106.0.5249.119 Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
}

REQUEST = requests.get('https://stage.ruscore.ru/2026-02-03', headers=headers)
soup = BeautifulSoup(REQUEST.content, 'html.parser')

seo_title = soup.find('title')
seo_description = soup.find('meta', attrs={'name': 'description'})
seo_h1 = soup.find('h1')


print("TITLE:", seo_title.text if seo_title else "❌ нет")
print("DESCRIPTION:", seo_description["content"] if seo_description else "❌ нет")
print("H1:", seo_h1.text if seo_h1 else "❌ нет")
