
# Módulos
from requests import get
from slugify import slugify
from bs4 import BeautifulSoup

# Formatando texto para slug
def Slug(text: str) -> str:
    return slugify(text)

# Replaces múltiplos
def multiReplaces(text: str, replaces: dict) -> str:
    for k, v in replaces.items():
        text = text.replace(k, v)
    return text

# Pegar BeautifulSoup4 do conteúdo
def Soup(url: str) -> BeautifulSoup:
    return BeautifulSoup(get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }).content, "html.parser")

# Pegar "Cards" do conteúdo
def Cards(url: str) -> list:
    return [{
        "SID": multiReplaces(i['data-src'], {"https://animefire.net/img/animes/": "", ".webp?v=1": ""}),
        "title": i["alt"],
        "image": i["data-src"]
    } for i in Soup(url).find_all("img", {"class": "imgAnimes"})]
