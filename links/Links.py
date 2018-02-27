from urllib import parse
from bs4 import BeautifulSoup

def parse_link( response):
    soup= BeautifulSoup(response.content,"html.parser")
    anchour=soup.findAll(name="a")
    seed=set()
    for n in anchour:
        base_link=str(n.get("href"))
        if base_link.find("#") != 0:
            base_link=parse.urljoin(response.url, base_link, allow_fragments=True)
            seed.add(base_link)

    #seed=set(seed)
    print(seed)
    return seed
