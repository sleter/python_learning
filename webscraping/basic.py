import bs4 as  bs
import urllib.request

sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = bs.BeautifulSoup(sauce,'lxml')

print(soup.title)
print(soup.name.title)
print(soup.title.string)
print(soup.p)

for p in soup.find_all('p'):
    print(p.string) # work when there is no child tags inside / use .text instead

print(soup.get_text()) # reads not only paragraphs

for url in soup.find_all('a'):
    print(url.get('href'))