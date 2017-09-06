import bs4 as bs
import urllib.request


sauce = urllib.request.urlopen('https://stackoverflow.com/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

for s in soup.find_all('a'):
    print(s.string)

