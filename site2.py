import requests as r
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/forms/'

def extraire_pages (url) :
 response = r.get(url)
 if response.status_code == 200 :
  soup = BeautifulSoup(response.content, 'html.parser')
  for s in range (1,11) :
   Url_page = f'https://www.scrapethissite.com/pages/forms/?page={s}'
   print (Url_page)
 else :
      print('echec', url)

extraire_pages(url)
response = r.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

