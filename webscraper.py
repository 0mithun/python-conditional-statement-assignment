from urllib.request import urlopen

from bs4 import BeautifulSoup as b


base_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="

request = 'xbox'
url_separator = '_sacat=0&_ipg=200&_pgn='
page = '317'

#url = base_url + request + url_separator + page
url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=ps4&_sacat=0&rt=nc&_ipg=25&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&rt=nc&_pgn=317&rt=nc'

html= urlopen(url).read()


soup = b(html,'html.parser')


result = soup.find_all('a', attrs={'aria-disabled': 'true'})
if(result):
    print("Last Page")
else:
    print("Not Last Page")


"""
for post in soup.find_all('li', attrs={'class': 's-item'}):
    single_post = post.find_all('a', attrs={'class': 's-item__link'})[0]
    title = single_post.text
    link = single_post['href']

    print(title)
    print(link)
    print()
"""



