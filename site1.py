import requests as rs
from bs4 import BeautifulSoup

Url = 'https://www.scrapethissite.com/pages/simple/'
s = rs.Session ()
r = s.get(Url)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup)




