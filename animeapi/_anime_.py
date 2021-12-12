
# Módulos
from ._utils_ import Soup

# Anime
class Anime:

    def __init__(self, SID: str) -> None:
        global soup
        self.SID = SID

        soup = Soup(f"https://animefire.net/animes/{SID}-todos-os-episodios")

    # Métodos
    def image(self) -> str:
        return soup.find("div", {"class": "sub_animepage_img"}).img["data-src"]

    def genres(self) -> list:
        return [i.text for i in soup.find_all("a", {"class": "spanGenerosLink"})]

    def trailer(self) -> str:
        return soup.find("div", {"id": "iframe-trailer"}).iframe["data-src"].split("?")[0]

    def titles(self) -> str:
        return [i.text for i in soup.find("div", {"class": "mr-2 d-inline-block div_anime_names"}).children if not len(i.text) <= 1]

    def ep(self, episode: int):

        # Módulos
        from json import loads
        from ._errs_ import InvalidNumber

        if not episode >= 1:
            raise InvalidNumber("episode")

        try:
            return loads(Soup(f"https://animefire.net/video/{self.SID}/{episode}").prettify())["data"][0]["src"]
        except IndexError:
            return None

    def rank(self) -> dict:

        # Módulos
        from ._utils_ import multiReplaces

        score = soup.find("h4", {"id": "anime_score"}).text
        return {
            "score": float(score) if not score == "N/A" else 0,
            "votes": int(multiReplaces(soup.find("h6", {"id": "anime_votos"}).text, {" votos": "",",": ""}))
        }

    # Classe
    def __str__(self) -> str:
        return self.titles()[0]

    def __repr__(self) -> str:
        return f"Anime({self.SID})"

    def __getitem__(self, key: str) -> str:
        from ._variables_ import animeinf
        from ._utils_ import multiReplaces
        from ._errs_ import InvalidKeyOrValue

        try:
            for tag in soup.find_all("div", {"class": ["animeInfo", "divSinopse"]}):
                if animeinf[key] == multiReplaces(str(tag.b), {"<b>": "", "</b>": ""}):
                    return tag.span.text.strip()
        except KeyError:
            raise InvalidKeyOrValue