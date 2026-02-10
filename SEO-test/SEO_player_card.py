import requests
from bs4 import BeautifulSoup



HEADERS = {
    'UserAgent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview Analytics) Chrome/106.0.5249.119 Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}

URL = ('https://stage.ruscore.ru/2026-01-01')

request = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(request.content, 'html.parser')

seo_title = soup.find('title')
seo_description = soup.find('meta', attrs={'name': 'description'})
seo_h1 = soup.find('h1')
seo_text = soup.select_one("p._description_10vpo_22")


print("TITLE:", seo_title.text if seo_title.text else "❌ нет")
print("DESCRIPTION:", seo_description["content"] if seo_description else "❌ нет")
print("H1:", seo_h1.text if seo_h1.text != '' else "❌ нет")
print("SEO-text:", seo_text.text if seo_text.text else "❌ нет")









