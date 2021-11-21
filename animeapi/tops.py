
# Módulos
from ._utils_ import Soup, Slug

# Inicialização
def Init(**args) -> list:
    return [{
        "highlight": f"https://{tag.img['src'][2:]}",
        "SID":  Slug(tag.img["alt"])
    } for tag in Soup("https://betteranime.net").find_all("div", {"class": "highlight-img"})]